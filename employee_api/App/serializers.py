from rest_framework import serializers
from . models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    employee_email=serializers.EmailField()
    password=serializers.CharField()