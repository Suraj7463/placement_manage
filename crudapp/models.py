from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    subject1=models.IntegerField()
    subject2=models.IntegerField()
    
