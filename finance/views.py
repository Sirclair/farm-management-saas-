from rest_framework import viewsets
from finance.models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(farm=self.request.user.farm)

    def perform_create(self, serializer):
        serializer.save(farm=self.request.user.farm)

class IncomeViewSet(viewsets.ModelViewSet):
    serializer_class = IncomeSerializer

    def get_queryset(self):
        return Income.objects.filter(farm=self.request.user.farm)

    def perform_create(self, serializer):
        serializer.save(farm=self.request.user.farm)