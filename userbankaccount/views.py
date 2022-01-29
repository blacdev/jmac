# from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from .serializers import Add_List_AccountSerializer
# from .models import BankaccountInfo
# from rest_framework import permissions
# from .permissions import IsOwner
# Create your views here.


# class Add_List_AccountAPIView(ListCreateAPIView):
#     Serializer_class = Add_List_AccountSerializer
#     queryset = BankaccountInfo.objects.all()
#     permissions_classes = (permissions.IsAuthenticated,)

    
#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)




# class Account_DetailAPIView(ListCreateAPIView):
#     Serializer_class = Add_List_AccountSerializer
#     queryset = BankaccountInfo.objects.all()
#     permissions_classes = (permissions.IsAuthenticated,IsOwner,)
#     lookup_field = 'account_id'


#     def perform_create(self, serializer):
#         return serializer.save(user=self.request.user)

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.decorators import api_view
import os
import requests
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from rest_framework import status

from userbankaccount.serializers import *


@swagger_auto_schema(
    methods=["post"],
    request_body=MonoUserExchangeSerializer,
    operation_summary="Creates and get messages",
    responses={200: "Success:succes", 400: "Error: Bad Request"},)
@api_view(['POST'])
def UserExchangeAPIView(request):

    data = request.data
    print(data)
    serializer = MonoUserExchangeSerializer(data = data) 

    if serializer.is_valid(raise_exception=True):
        
        
        print(data)
        url = "https://api.withmono.com/account/auth"

        payload = {"code": data["code"]}
        headers = {
            "Accept": "application/json",
            "mono-sec-key": os.environ.get("MONO_SEC_KEY") ,
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response)
        
        

        return Response(response, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




test_param = openapi.Parameter('id', openapi.IN_QUERY, description="user bank id", type=openapi.TYPE_STRING)
user_response = openapi.Response('response description', MonoUserInformationSerializer)
@swagger_auto_schema(method='get', manual_parameters=[test_param], responses={200: user_response})
@api_view(['GET'])
def UserInfoAPIView(request):

    data = request.GET.get('id')
    print(data)
    serializer = MonoUserInformationSerializer(data = data) 

    if serializer.is_valid(raise_exception=True):
        
        
        print(data)
        url = "https://api.withmono.com/account/"+ data["id"]

        headers = {
            "Accept": "application/json",
            "mono-sec-key": os.environ.get("MONO_SEC_KEY") ,
            "Content-Type": "application/json"
        }

        response = requests.request("GET", url, headers=headers)
        print(response)
        
        

        return Response(response, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
