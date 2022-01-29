from rest_framework import serializers
from userbankaccount.models import BankaccountInfo

class Add_List_AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankaccountInfo
        fields = ['account_id', 'bank_name', 'bank_account_number', 'bank_account_name', 'bank_account_type']


class UserExchangeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255)