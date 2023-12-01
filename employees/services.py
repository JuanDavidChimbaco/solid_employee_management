class EmployeeServices:
    def calculate_bonus(self, employee):
        if employee.position == 'Manager':
            return employee.salary * 0.2
        elif employee.position == 'Developer':
            return employee.salary * 0.1
        else:
            return 0
        