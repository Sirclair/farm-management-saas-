from django.db.models import Sum, F, FloatField
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from decimal import Decimal

from flock.models import FlockBatch, DailyRecord
from sales.models import OrderItem
from finance.models import Expense

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def farm_kpis(request):
    farm = request.user.farm

    # 1️⃣ Total birds received
    total_received = FlockBatch.objects.filter(farm=farm).aggregate(
        total=Sum("quantity_received")
    )["total"] or 0

    # 2️⃣ Total mortality
    total_mortality = DailyRecord.objects.filter(flock__farm=farm).aggregate(
        total=Sum("mortality")
    )["total"] or 0

    # 3️⃣ Total birds sold (from orders that are paid)
    total_sold = OrderItem.objects.filter(
        order__farm=farm,
        order__is_paid=True
    ).aggregate(total=Sum("quantity"))["total"] or 0

    # 4️⃣ Birds still in cages
    birds_alive = total_received - total_mortality - total_sold
    if birds_alive < 0:
        birds_alive = 0  # safety check

    # 5️⃣ Total feed used
    total_feed = DailyRecord.objects.filter(flock__farm=farm).aggregate(
        total=Sum("feed_used_kg")
    )["total"] or 0

    # 6️⃣ Total revenue
    revenue = OrderItem.objects.filter(
        order__farm=farm, order__is_paid=True
    ).annotate(item_total=F("quantity") * F("price")).aggregate(
        total=Sum("item_total", output_field=FloatField())
    )["total"] or 0

    # 7️⃣ Total expenses
    expenses = Expense.objects.filter(farm=farm).aggregate(
        total=Sum("amount")
    )["total"] or 0

    # 8️⃣ Net profit
    net_profit = float(revenue) - float(expenses)

    return Response({
        "total_received": total_received,
        "total_mortality": total_mortality,
        "birds_sold": total_sold,
        "birds_alive": birds_alive,
        "total_feed_used_kg": total_feed,
        "revenue": revenue,
        "expenses": expenses,
        "net_profit": net_profit,
    })