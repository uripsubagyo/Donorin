from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class hasilScreening(models.Model):
    namaDonor = models.CharField(max_length=255)
    suhuTubuh = models.IntegerField()
    tekananDarah = models.IntegerField()
    kadarHemo = models.IntegerField()
    beratBadan = models.IntegerField()
    