from django.shortcuts import render
from .models import Employee
from .services import EmployeeServices

from rest_framework import generics
from rest_framework.response import Response

from .serializers import EmployeeSerializer

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    employee_service = EmployeeServices()
    bonuses = [employee_service.calculate_bonus(emp) for emp in employees]
    
    context = {'empleados':zip(employees,bonuses)}
    return render(request, 'employees/employee_list.html', context)