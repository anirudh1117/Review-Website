from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
CHOICES=(('Default','Default'),('fb','Facebook'),('G','Google'),)
class UserProfile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNo = models.DecimalField(max_digits=10, decimal_places=0)
    provider = models.CharField(max_length=20,choices=CHOICES,default="Default")

