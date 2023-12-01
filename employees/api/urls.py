from django.urls import path
from .views import EmployeeListAPIView, EmployeeAddAPIView, EmployeeUpdateAPIView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='empployee-list-api'),
    path('employees/create/', EmployeeAddAPIView.as_view(), name="employee-create-api"),
    path('employees/update/<int:id>/', EmployeeUpdateAPIView.as_view(), name="employee-update-api"),
]
