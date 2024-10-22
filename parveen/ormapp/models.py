from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
 name=models.CharField(max_length=100)
age=models.IntegerField()
ac=models.IntegerField(primary_key="ac")
customerid=models.IntegerField()
income=models.IntegerField()

class BankloanAdmin(admin.ModelAdmin):
 list_dispaly=('name','age','ac','customerid','income')

