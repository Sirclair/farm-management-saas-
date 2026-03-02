from django.contrib import admin
from .models import Order, OrderItem
from django.utils.html import format_html


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "farm",
        "flock",
        "customer_name",
        "is_paid",
        "created_at",
        "updated_at",
        "order_total_display",
    )
    list_filter = ("farm", "flock", "is_paid")
    search_fields = ("customer_name", "flock__name")

    def order_total_display(self, obj):
        return obj.order_total
    order_total_display.short_description = "Order Total"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product_name", "quantity", "price", "total_price_display")
    list_filter = ("order__farm",)
    search_fields = ("product_name", "order__customer_name")

    def total_price_display(self, obj):
        return obj.total_price
    total_price_display.short_description = "Item Total"