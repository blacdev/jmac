from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .serializers import accountRegisterSerializers, EmailVerificationSerializer, loginSerializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Accounts
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi

# Create your views here.

class accountRegisterView(generics.GenericAPIView):
    """
    This endpoint allows you to register a new user.
    With the following data:
    {
        "username": "username",
        "email": "user email",
        "password": "user password"
    }
    The repons is a messge that tells you if that an email has been sent to your email address.
    """
    serializer_class = accountRegisterSerializers

    def post(self, request, *args, **kwargs):
        user  = request.data
        serializer = self.get_serializer(data=user) 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            print(user_data) # to deletelater
            user = Accounts.objects.get(username = user_data["username"],email=user_data['email'])
            print(user) # to deletelater
            print(user.id) # to deletelater
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_url = reverse("account-email-verify")
            absUrls = "http://" + current_site + relative_url + "?token=" + str(token)
            email_body = "hi " + user.username + "\n, please use this link below to verify your email. \n" + absUrls
            Email_data = {"email_body":email_body, "to_email":user.email, "email_subject":"Verify your email address",}
            Util.send_email(Email_data)
            Util.send_email(Email_data)
            data = {"message":"A verification email has been sent to your email address.",

                }
            return Response(data, status=status.HTTP_201_CREATED)
        data = {"message":"Email could not be sent"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter("token", in_=openapi.IN_QUERY, description="token", type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print(payload)
            user = Accounts.objects.get(id=payload['user_id'])
            print(user)
            print(user.id)
            print(user.is_verified)
            if   (user.is_verified == False):
                user.is_verified = True
            if (user.is_active == False):
                user.is_active = True
            print(user.is_verified)
            user.save()
            return Response({"Emial":"Sucessfully activated"}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({"Error":"Activation expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({"Error":"Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = loginSerializers


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        