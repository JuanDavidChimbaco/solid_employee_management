from rest_framework import generics
from rest_framework.response import Response

from ..serializers import EmployeeSerializer
from ..models import Employee
from ..services import EmployeeServices

class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def list(self, request, *args, **kwargs):
        employees = self.get_queryset()
        employee_services = EmployeeServices()
        data = [{
            'id':emp.id,
            'name':emp.name,
            'position':emp.position, 
            'salary':emp.salary, 
            'bonus':employee_services.calculate_bonus(emp)
            } for emp in employees]
        return Response(data)