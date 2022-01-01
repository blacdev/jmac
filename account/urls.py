from django.urls import path
from .views import *



urlpatterns = [
    path('account/', accountRegisterView.as_view(), name='account-register'),
    path("account/email-verify", VerifyEmail.as_view(), name="account-email-verify"),
]