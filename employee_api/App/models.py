from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_regNo=models.TextField(unique=True)
    employee_name=models.CharField(max_length=200)
    employee_email=models.EmailField(max_length=200)
    employee_mobile=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=250)