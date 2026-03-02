from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlockBatchViewSet, DailyRecordViewSet

router = DefaultRouter()
router.register(r"flocks", FlockBatchViewSet)
router.register(r"daily-records", DailyRecordViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
