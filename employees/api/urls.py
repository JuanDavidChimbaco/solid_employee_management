from django.urls import path
from .views import EmployeeListAPIView

urlpatterns = [
    path('employees/', EmployeeListAPIView.as_view(), name='empployee-list-api'),
]
