from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

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
    
class EmployeeAddAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'id'