# flock/models.py
from django.db import models
from django.utils import timezone
from accounts.models import Farm

class FlockBatch(models.Model):
    name = models.CharField(max_length=255)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="flock_batches")
    quantity_received = models.PositiveIntegerField()
    status = models.CharField(
        max_length=50,
        choices=(("active", "Active"), ("sold", "Sold"), ("closed", "Closed"))
    )
    date_received = models.DateField(default=timezone.now)

    # Purchase info
    price_per_bird = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    supplier = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    feed_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.name} ({self.farm.name})"


class DailyRecord(models.Model):
    flock = models.ForeignKey(FlockBatch, on_delete=models.CASCADE, related_name="daily_records")
    date = models.DateField(default=timezone.now)
    mortality = models.PositiveIntegerField(default=0)
    feed_used_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.flock.name} - {self.date}"