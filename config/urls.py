from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/refresh/", TokenRefreshView.as_view(), name="refresh"),

    # App URLs
    path("api/", include("accounts.urls")),
    path("api/flock/", include("flock.urls")),
    path("api/sales/", include("sales.urls")),
    path("api/finance/", include("finance.urls")),
    path("api/dashboard/", include("dashboard.urls")),
]