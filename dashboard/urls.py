from django.urls import path
from .views import farm_kpis

urlpatterns = [
    path("kpis/", farm_kpis),
]