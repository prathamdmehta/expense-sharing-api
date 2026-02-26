from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, ExpenseViewSet

# Automatic URL router for API endpoints
router = DefaultRouter()
router.register(r'groups', GroupViewSet)    # /api/groups/
router.register(r'expenses', ExpenseViewSet) # /api/expenses/

# All API endpoints generated automatically
urlpatterns = [path('', include(router.urls))]