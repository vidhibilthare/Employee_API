from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from . models import *
from. serializers import EmployeeSerializer
from. serializers import LoginSerializer
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class EmployeeCreateAPI(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeAPI(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UpdateEmployeeAPI(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RetrieveEmployeeAPI(generics.RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer


class DeleteEmployeeAPI(generics.DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class = EmployeeSerializer

class RegistrationAPI(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self,request):
        data = request.POST.copy()
        password = data.get('password')
        data['password']=make_password(password)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        employee=serializer.save()
        refresh = RefreshToken.for_user(employee)
        Token={
            'refresh' : str(refresh),
            'access' : str(refresh.access_token)
        }
        return Response (Token)
    
class LoginAPIView(generics.CreateAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)

        employee_email = serializers.validated_data['employee_email'] 
        password = serializers.validated_data['password']
        try:
            employee = Employee.objects.get(employee_email=employee_email)
        except Employee.DoesNotExist:
            return Response({'error':'Invalid email.'},status=400)
        if not check_password(password,employee.password):
            return Response({'error':'invalid password.'},status=400)
        refresh = RefreshToken.for_user(employee)
        response_data={
            'email':employee_email,
            'access_token' : str(refresh.access_token),
        }
        return Response(response_data)