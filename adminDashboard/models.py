from django.db import models
from django.contrib.auth.models import User
from users.models import UserAccount
from users.models import MyAccountManager

# Create your models here.
class hasilScreening(models.Model):
    namaDonor = models.CharField(max_length=255)
    suhuTubuh = models.IntegerField()
    tekananDarah = models.IntegerField()
    kadarHemo = models.IntegerField()
    beratBadan = models.IntegerField()
    