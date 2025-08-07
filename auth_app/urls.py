# auth_app/urls.py
from django.urls import path
from .views import (
    SignupView,
    LoginView,
    ProtectedView,
    TokenRefreshView,
    LoginPageView,
    SignupPageView,
    DashboardPageView,
)

urlpatterns = [
    path("api/auth/signup/", SignupView.as_view(), name="signup"),
    path("api/auth/login/", LoginView.as_view(), name="login"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/protected/", ProtectedView.as_view(), name="protected"),
    # Web views
    path("login/", LoginPageView.as_view(), name="login_page"),
    path("signup/", SignupPageView.as_view(), name="signup_page"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard_page"),
]
