from .models import Accounts
from rest_framework import serializers


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