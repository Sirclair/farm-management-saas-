from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import current_user, FarmViewSet

router = DefaultRouter()
router.register(r"farms", FarmViewSet, basename="farm")

urlpatterns = [
    path("me/", current_user, name="current_user"),
    #path("register/", UserRegisterView.as_view(), name="register"),
    path("", include(router.urls)),
]