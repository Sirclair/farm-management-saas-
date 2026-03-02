from django.db import models
from accounts.models import Farm

class ExpenseCategory(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="expense_categories")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("farm", "name")

    def __str__(self):
        return f"{self.name} ({self.farm.name})"


class Expense(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="expenses")
    category = models.ForeignKey(ExpenseCategory, on_delete=models.PROTECT, related_name="expenses")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.amount} - {self.category.name} ({self.farm.name})"