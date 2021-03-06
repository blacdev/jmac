from django.urls import path
from .views import *



urlpatterns = [

    path('account/register', accountRegisterView.as_view(), name='account-register'),
    path('account/login', LoginView.as_view(), name="Login"),

    path("account/email-verify", VerifyEmail.as_view(), name="account-email-verify"),
]