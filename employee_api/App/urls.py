from django.urls import path
from . views import *

urlpatterns = [
    path('',EmployeeAPI.as_view()),
    path('create/',EmployeeCreateAPI.as_view()),
    path('Update/<int:pk>',UpdateEmployeeAPI.as_view()),
    path('Delete/<int:pk>',DeleteEmployeeAPI.as_view()),
    path('Get/<int:pk>',RetrieveEmployeeAPI.as_view()),
    path('registration/',RegistrationAPI.as_view())
]
