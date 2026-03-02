from django.contrib import admin
from .models import Expense, ExpenseCategory

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "farm", "description", "created_at", "updated_at")
    search_fields = ("name", "farm__name")

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    # Use fields that actually exist in Expense model
    list_display = ("id", "farm", "category", "amount", "description", "created_at")
    list_filter = ("farm", "category", "created_at")
    search_fields = ("farm__name", "category__name", "description")