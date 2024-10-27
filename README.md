# Ex02 Django ORM Web Application
## Date: 26:10:2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

[text](<../Pictures/NEW BANK LOAN.drawio>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from.models import Bankloan,BankloanAdmin 
admin.site.register(Bankloan,BankloanAdmin)
```


## OUTPUT
![alt text](screenshot-1729602670000.png)

Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
