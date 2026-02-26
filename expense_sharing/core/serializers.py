from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group, Expense


class UserSerializer(serializers.ModelSerializer):
    """
    Converts User model to JSON for API responses.
    Used in GroupSerializer to show group members.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class GroupSerializer(serializers.ModelSerializer):
    """
    Main serializer for groups. 
    Shows group details + all members (using UserSerializer).
    """
    members = UserSerializer(many=True, read_only=True)  # Show all group members
    
    class Meta:
        model = Group
        fields = ['id', 'name', 'members', 'created_at']


class ExpenseListSerializer(serializers.ModelSerializer):
    """
    Used for LIST view (GET /api/expenses/).
    Read-only display of expenses with friendly names.
    """
    group_name = serializers.CharField(source='group.name', read_only=True)  # Shows group name instead of ID
    paid_by_username = serializers.CharField(source='paid_by.username', read_only=True)  # Shows username instead of ID
    
    class Meta:
        model = Expense
        fields = ['id', 'group', 'group_name', 'description', 'amount', 'paid_by', 'paid_by_username', 'created_at']


class ExpenseSerializer(serializers.ModelSerializer):
    """
    Used for CREATE/UPDATE (POST/PATCH /api/expenses/).
    Handles form input + validation.
    """
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())  # Dropdown of all groups
    paid_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)  # Optional user dropdown
    group_name = serializers.CharField(source='group.name', read_only=True)  # Display only
    paid_by_username = serializers.CharField(source='paid_by.username', read_only=True)  # Display only
    
    class Meta:
        model = Expense
        fields = ['id', 'group', 'group_name', 'description', 'amount', 'paid_by', 'paid_by_username', 'created_at']

    def validate(self, data):
        """
        MAIN VALIDATION: Runs when user submits form.
        1. If no paid_by selected → use current logged-in user
        2. Check if selected user belongs to selected group
        """
        request = self.context.get('request')  # Get current logged-in user
        group = data.get('group')  # Group selected by user
        paid_by = data.get('paid_by')  # User selected by user (or None)
        
        # Rule 1: No selection = use current user
        if not paid_by:
            paid_by = request.user  # Default to who is creating expense
            data['paid_by'] = paid_by
        
        # Rule 2: Must be group member
        if group and paid_by:
            group_members = group.members.all()  # Get all allowed users
            if paid_by not in group_members:  # Check membership
                raise serializers.ValidationError("Selected user is not in this group!")
        
        return data  # Validation passed!

    def validate_amount(self, value):
        """
        Check amount field individually.
        Runs for both create AND update.
        """
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive!")
        if value > 10000:  # Business rule: no huge expenses
            raise serializers.ValidationError("Amount too high!")
        return value

    def validate_description(self, value):
        """
        Clean and validate description field.
        Ensures meaningful descriptions.
        """
        if len(value.strip()) < 3:  # Remove whitespace, check length
            raise serializers.ValidationError("Description too short!")
        return value.strip()  # Return cleaned version