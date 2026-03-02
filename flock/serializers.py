# flock/serializers.py
from rest_framework import serializers
from .models import FlockBatch, DailyRecord

class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = ["id", "date", "mortality", "feed_used_kg"]

class FlockBatchSerializer(serializers.ModelSerializer):
    daily_records = DailyRecordSerializer(many=True, read_only=True)

    class Meta:
        model = FlockBatch
        fields = [
            "id",
            "name",
            "date_received",
            "quantity_received",
            "status",
            "price_per_bird",
            "total_price",
            "supplier",
            "contact_number",
            "location",
            "feed_price_per_kg",
            "daily_records",
        ]