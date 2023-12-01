from django.shortcuts import get_object_or_404, render, redirect
from .models import Employee
from .services import EmployeeServices
from .forms import EmployeeForm

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    employee_service = EmployeeServices()
    bonuses = [employee_service.calculate_bonus(emp) for emp in employees]
    
    context = {'empleados':zip(employees,bonuses)}
    return render(request, 'employees/employee_list.html', context)

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
        
    return render(request, 'employees/add_employee.html', {'form':form})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
        
    return render(request, 'employees/edit_employee.html', {'form':form})