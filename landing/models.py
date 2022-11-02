from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=255)
    description = models.TextField()
