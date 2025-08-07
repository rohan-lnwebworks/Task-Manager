# views.py
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import UserSignupSerializer, CustomTokenObtainPairSerializer
from django.views.generic import TemplateView


class SignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]


class TokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        display_name = request.user.name or request.user.username
        return Response({"message": f"Hello {display_name}, you are authenticated."})


# Class-based template views
class LoginPageView(TemplateView):
    template_name = "auth/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Login"
        return context


class SignupPageView(TemplateView):
    template_name = "auth/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Sign Up"
        return context


class DashboardPageView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Dashboard"
        return context


class HomePageView(TemplateView):
    template_name = "auth/login.html"
