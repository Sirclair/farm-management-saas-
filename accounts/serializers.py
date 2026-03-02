from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import Farm
from flock.models import FlockBatch, DailyRecord

User = get_user_model()

class DailyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyRecord
        fields = "__all__"

class FlockSerializer(serializers.ModelSerializer):
    daily_records = DailyRecordSerializer(many=True, read_only=True)

    class Meta:
        model = FlockBatch
        fields = "__all__"

class FarmSerializer(serializers.ModelSerializer):
    flocks = FlockSerializer(many=True, read_only=True)

    class Meta:
        model = Farm
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    farms = FarmSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "farms"]