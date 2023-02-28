from django.db import models

# Create your models here.

class Studentdata(models.Model):
    ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=50)
    SURNAME = models.CharField(max_length=15)
