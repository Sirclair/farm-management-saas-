from django.contrib import admin
from django.db.models import Sum, F, DecimalField
from decimal import Decimal
from django.utils.html import format_html
from .models import FlockBatch, DailyRecord
from sales.models import Order, OrderItem
from finance.models import Expense
import datetime

@admin.register(FlockBatch)
class FlockBatchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "farm",
        "quantity_received",
        "status",
        "date_received",
        "total_revenue",
        "total_expenses",
        "profit",
        "orders_link",
        "expenses_link",
    )
    list_filter = ("status", "farm")
    search_fields = ("name",)

    # --- Financial columns ---
    def total_revenue(self, obj):
        revenue = (
            OrderItem.objects.filter(order__farm=obj.farm, order__flock=obj)
            .annotate(item_total=F("quantity") * F("price_per_bird"))
            .aggregate(total=Sum("item_total", output_field=DecimalField()))["total"]
        ) or Decimal("0.00")
        return round(revenue, 2)
    total_revenue.short_description = "Revenue"

    def total_expenses(self, obj):
        expenses = (
            Expense.objects.filter(farm=obj.farm)
            .aggregate(total=Sum("amount"))["total"]
        ) or Decimal("0.00")
        return round(expenses, 2)
    total_expenses.short_description = "Expenses"

    def profit(self, obj):
        return round(self.total_revenue(obj) - self.total_expenses(obj), 2)
    profit.short_description = "Profit"

    # --- Links to related objects ---
    def orders_link(self, obj):
        count = Order.objects.filter(order__flock=obj).count()
        return format_html(
            '<a href="/admin/sales/order/?flock__id__exact={}">{} Orders</a>', obj.id, count
        )
    orders_link.short_description = "Orders"

    def expenses_link(self, obj):
        count = Expense.objects.filter(farm=obj.farm).count()
        return format_html(
            '<a href="/admin/finance/expense/?farm__id__exact={}">{} Expenses</a>', obj.farm.id, count
        )
    expenses_link.short_description = "Expenses"


@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "flock", "date", "mortality", "feed_used_kg")
    list_filter = ("date", "flock")
    search_fields = ("flock__name",)