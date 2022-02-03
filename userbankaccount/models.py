from django.db import models
from account.models import Accounts

# Create your models here.


class BankaccountInfo(models.Model):
    account_id           = models.CharField(max_length=255, null=False, blank=False)
    user                 = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    bank_name            = models.CharField(max_length=30, null=False, blank=False)
    bank_account_number  = models.CharField(max_length=30, null=False, blank=False)
    bank_account_name    = models.CharField(max_length=30, null=False, blank=False)
    bank_account_type    = models.CharField(max_length=30, null=False, blank=False)
    user_bvn             = models.CharField(max_length=255, null=False, blank=False)
    bank_code            = models.CharField(max_length=255, null=False, blank=False)
    bank_type            = models.CharField(max_length=255, null=False, blank=False)


    def __str__(self):
        return self.user
