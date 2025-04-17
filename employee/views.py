from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import JsonResponse



def employee_table(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_table.html', {'employees': employees})

def add_employee(request):
    if request.user is None:
        """not authenticated"""
        return JsonResponse({'error': 'not authenticated'}, 401)
    
    if request.method == 'POST':
        data = request.POST.copy()
        print("data-data::", data)
        data['createBy'] = request.user
        form = EmployeeForm(data)

        print("request_post:", data)
        print("Form errors:", form.errors)
        if form.is_valid():
            emp = form.save()
            return redirect('employee_table')
        
    return JsonResponse({'error': 'Invalid form'}, status=400)