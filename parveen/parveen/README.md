## Ex02 Django ORM Web Applications
## DATE:27.10.2024

## AIM
  To develop a Djangp Application to atore and retrieve data from a banl loan database using Object Relational Mapping(ORM).




## ENTITY RELATIONSHIP DIAGRAM
[text](<../../../Pictures/Untitled Diagram.drawio>)


## DESIGN STEPS

STEP 1:

CLONE THE PROBLEM FROM GITHUB

STEP 2:

CREATE A NEW APP IN dJANGO PROJECT

STEP 3:

ENTER THE CODE FOR admin.py AND models.py

STEP 4:

EXECUTE DJANGO ADMINAND CREATE DETAILS FOR 10 BOOKS


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
![alt.text](<"C:\Users\mouli\Pictures\screenshot-1729602670000.png">)
   
## RESULT

Thus the program for creating a database using ORM has been executed successfully.

