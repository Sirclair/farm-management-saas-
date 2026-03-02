from rest_framework import serializers
from finance.models import Expense, Income

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ("farm",)

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        exclude = ("farm",)