from django.shortcuts import render
from rest_framework import generics, status
from .serializers import accountRegisterSerializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Accounts
from .utils import send_email
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

# Create your views here.

class accountRegisterView(generics.GenericAPIView):
    serializer_class = accountRegisterSerializers

    def post(self, request, *args, **kwargs):
        user  = request.data
        serializer = self.get_serializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = Accounts.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_url = reverse("account-email-verify")
        absUrls = "http://" + current_site + relative_url + "?token=" + str(token)
        email_body = "hi " + user.username + ", please click the link below to verify your email address. " + absUrls

        data = {"email_body":email_body, "to_email":user.email, "email_subject":"Verify your email address",}
        send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Accounts.objects.get(email=payload['email'])
            user.is_verified = True
            user.save()
            return Response({"emial":"Sucessfully activated"}, status=status.HTTP_200_OK)
        except:
            return Response({"message":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)





