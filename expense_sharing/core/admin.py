from django.contrib import admin
from .models import Group, Expense

class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['description', 'group', 'amount', 'paid_by']
    list_filter = ['group', 'created_at']

admin.site.register(Group, GroupAdmin)
admin.site.register(Expense, ExpenseAdmin)
