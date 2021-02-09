import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Serviceuser(models.Model):
	name = models.CharField(max_length=200)
	nid_no = models.CharField(max_length=200)
	date_created = models.CharField(max_length=200)
	balance = models.IntegerField(default=0)

	def __str__(self):
		return self.name


class Deposit(models.Model):
	serviceuser = models.ForeignKey(Serviceuser,on_delete=models.CASCADE)
	deposit_amount = models.IntegerField()

class Withdraw(models.Model):
	serviceuser = models.ForeignKey(Serviceuser,on_delete=models.CASCADE)
	withdraw_amount = models.IntegerField()

class SendMoney(models.Model):
	serviceuser = models.ForeignKey(Serviceuser,on_delete=models.CASCADE)
	amount = models.IntegerField()


