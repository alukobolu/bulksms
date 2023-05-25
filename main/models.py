# from django.db import models

# # Create your models here.

# class SentMessages(models.Model) :

#     user = models.ForeignKey(User, null=True, on_delete=CASCADE)
#     trasaction_account_institution =  models.CharField(max_length=200, null=True, blank=True)
#     transaction_account_id = models.CharField(max_length=250, null=True,  blank=True)
#     transaction_id = models.CharField(max_length=250, null=True,  blank=True, unique = True )
#     transaction_type = models.CharField(max_length=250, null=True,  blank=True)