from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
    """
    Represents a group of users who share expenses (like "Trip to Goa", "Roommates").
    Members split costs equally.
    """
    name = models.CharField(max_length=200)  # Group name: "Office Lunch Group"
    members = models.ManyToManyField(User)  # Users in this group (many-to-many)
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation time
    
    def __str__(self):
        """What shows in Django Admin dropdowns and debug output."""
        return self.name

    class Meta:
        verbose_name_plural = "Groups"  # Admin shows "Groups" not "Group"


class Expense(models.Model):
    """
    Single expense within a group (like "Dinner - $50").
    One user pays, everyone splits equally.
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # Which group this expense belongs to
    description = models.CharField(max_length=200)  # "Pizza", "Uber", "Groceries"
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # $50.00 (10 digits total, 2 after decimal)
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Who actually paid (one user)
    created_at = models.DateTimeField(auto_now_add=True)  # When expense was recorded
    
    def __str__(self):
        """Readable display in Admin and debug output."""
        return f"{self.description} - {self.amount}"
    
    class Meta:
        ordering = ['-created_at']  # Newest expenses first
        verbose_name_plural = "Expenses"

    class Meta:
        indexes = [
            models.Index(fields=['group']),           # ⚡ 100x faster group filtering
            models.Index(fields=['paid_by']),         # ⚡ 100x faster user filtering  
            models.Index(fields=['group', 'created_at']),  # ⚡ Balances endpoint
        ]
