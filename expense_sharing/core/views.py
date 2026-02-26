from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from decimal import Decimal
from .models import Group, Expense
from .serializers import (
    GroupSerializer, 
    ExpenseSerializer, 
    ExpenseListSerializer
)
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

class GroupViewSet(viewsets.ModelViewSet):
    """
    Handles all group operations: CRUD + custom actions.
    Full CRUD: GET/POST/PATCH/DELETE /api/groups/
    """
    queryset = Group.objects.all()  # All groups in database
    serializer_class = GroupSerializer  # Converts Group → JSON
    permission_classes = [IsAuthenticatedOrReadOnly]  # Login required for changes

    def perform_create(self, serializer):
        """
        Automatically adds creator as group member when creating new group.
        Runs ONLY during POST /api/groups/
        """
        group = serializer.save()  # Save group to database
        group.members.add(self.request.user)  # Add creator to members

    @method_decorator(cache_page(300)) # Cache balances for 5 minutes (300 seconds)
    @action(detail=True, methods=['get'])
    def balances(self, request, pk=None):
        """
        GET /api/groups/1/balances/ - Calculate who owes whom
        Formula: balance[username] = (money_paid) - (total_shares_owed)
        Positive = owed money, Negative = owes money, Zero = settled
        """
        group = self.get_object()  # Get specific group (pk=1)
        expenses = Expense.objects.filter(group=group).select_related('paid_by')[0:1000]  # All expenses in group
        
        member_count = group.members.count()  # How many people split costs
        balances = {member.username: Decimal(0) for member in group.members.all()}  # Zero balances
        
        for expense in expenses:  # For each expense
            share = expense.amount / member_count  # Everyone's share
            balances[expense.paid_by.username] += expense.amount  # Payer gets full amount back
            for username in balances:  # Everyone else owes their share
                if username != expense.paid_by.username:
                    balances[username] -= share
        
        return Response(balances)  # Return final balances

    @action(detail=True, methods=['post'], url_path='expenses')
    def add_expense(self, request, pk=None):
        """
        POST /api/groups/1/expenses/ - Create expense for THIS group only
        Automatically sets group ID - no need to specify in request
        """
        group = self.get_object()  # Specific group (pk=1)
        data = request.data.copy()  # Copy request data
        data['group'] = group.id  # Auto-fill group field
        
        serializer = ExpenseSerializer(data=data, context={'request': request})
        if serializer.is_valid():  # Run validation
            serializer.save()  # Save to database
            return Response(serializer.data)  # Success response
        return Response(serializer.errors, status=400)  # Validation errors

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    Handles all expense operations.
    Full CRUD: GET/POST/PATCH/DELETE /api/expenses/
    """
    queryset = Expense.objects.all()  # All expenses
    permission_classes = [IsAuthenticatedOrReadOnly]  # Login required for changes
    pagination_class = PageNumberPagination  # Handles 100s of expenses
    filterset_fields = ['group', 'paid_by']  # Filter: ?group=1&paid_by=2
    filter_backends = [DjangoFilterBackend]  # Enable filtering

    def get_serializer_class(self):
        """
        Use different serializers based on action:
        - LIST/RETRIEVE: ExpenseListSerializer (read-only display)
        - CREATE/UPDATE: ExpenseSerializer (form + validation)
        """
        if self.action == 'list':  # GET /api/expenses/
            return ExpenseListSerializer
        return ExpenseSerializer  # POST/PATCH/GET single

    def get_serializer_context(self):
        """
        Pass current request to serializer.
        Needed for validation (access request.user).
        """
        context = super().get_serializer_context()
        context['request'] = self.request  # Give serializer current user
        return context

    def perform_create(self, serializer):
        """
        Save expense without overriding user selection.
        Validation handles paid_by defaulting.
        """
        serializer.save()  # Let serializer decide paid_by
    
    def get_queryset(self):
        # Always prefetch for speed
        return Expense.objects.select_related('group', 'paid_by').all()

    