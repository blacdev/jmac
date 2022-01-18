from .models import Accounts
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class accountRegisterSerializers(serializers.ModelSerializer):

    password = serializers.CharField(min_length = 8, max_length = 68, write_only=True)

    class Meta:
        model = Accounts
        fields = ('username', 'email', 'password')
    
    def validate(self, attrs):
        email = attrs.get('email', "")
        username = attrs.get('username', "")
        password = attrs.get('password', "")
        id = attrs.get('id', "")

        if  not password.isalnum():
            raise serializers.ValidationError("password must be alphanumeric")
        # if email and Account.objects.filter(email=email).exists():
        #     raise serializers.ValidationError("Email already exists")
        # if username and Account.objects.filter(username=username).exists():
        #     raise serializers.ValidationError("Username already exists")
        return attrs
        
        # return super().validate(attrs)

    def create(self, validated_data):
        return Accounts.objects.create_user(**validated_data)


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=600, read_only=True)
    class Meta:
        model = Accounts
        fields = ('token',)

class loginSerializers(serializers.ModelSerializer):

    password    = serializers.CharField(min_length = 8, max_length = 68, write_only=True)
    class Meta:
        model = Accounts
        fields = ["username",'password', "token"]

    def validate(self, attrs):
        username = attrs.get('username', "")
        print(username)
        password = attrs.get('password', "")
        print(password)

        user = authenticate(username=username, password=password)
        
        
        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        if user.is_active is not True:
            raise AuthenticationFailed("Account disabled, please contact admin")
        
        if user.is_verified is not True:
            print(user.is_verified)
            raise AuthenticationFailed("Email is not verified")

        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            "token": user.token,
        }


        return super().validate(attrs)