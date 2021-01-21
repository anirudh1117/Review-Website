from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

# Create your models here.
CHOICES=(('Default','Default'),('fb','Facebook'),('G','Google'),)
class UserProfile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    phoneNo = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null=True)
    provider = models.CharField(max_length=20,choices=CHOICES,default="Default")

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_userprofile(sender,instance=None,created=False,**kwargs):
	if created:
		UserProfile.objects.create(user_id=instance)

