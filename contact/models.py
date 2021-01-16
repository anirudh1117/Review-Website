from django.db import models
from datetime import datetime
# Create your models here.
class Contact_table(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now,blank=True)