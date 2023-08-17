from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .serializers import CompanySerializer
from .models import Company, Employee
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CompanyForm, EmployeeForm, EmployeeDeleteForm, EmployeeUpdateForm
from django.contrib import messages


def home(request):
    return render(request, 'base.html')

@api_view(['POST', 'GET'])
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company added successfully')
            return redirect('get_company')
        else:
            messages.error(request, 'Error adding company. Please check the form.')
    else:
        form = CompanyForm()
    return render(request, 'add_company.html', {'form': form})

@api_view(['GET'])
def get_company(request):
    if request.method == 'GET':
        query = Company.objects.all()
        serializer = CompanySerializer(query, many=True)
        return render(request, 'get_company.html', {'companies': serializer.data})

@api_view(['GET'])
def update_company_list(request):
    companies = Company.objects.all()
    return render(request, 'update_company_list.html', {'companies': companies})

@api_view(['GET', 'POST'])
def update_company_form(request):
    if request.method == 'POST':
        company_id = request.GET.get('company_id')
        company = get_object_or_404(Company, id=company_id)
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company updated successfully')
            return redirect('get_company')  # Replace with the appropriate URL name
    else:
        form = CompanyForm()

    return render(request, 'update_company.html', {'form': form})


@api_view(['GET', 'POST'])
def delete_company_form(request):
    companies = Company.objects.all()

    if request.method == 'POST':
        company_id = request.POST.get('company')
        company = get_object_or_404(Company, id=company_id)
        company.delete()
        messages.success(request, 'Company deleted successfully')
        return redirect('get_company')

    return render(request, 'delete_company.html', {'companies': companies})


@api_view(['POST', 'GET'])
def add_emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee added successfully')
            return redirect('get_emp')
        else:
            messages.error(request, 'Error adding employee. Please check the form.')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'employee_form': form})

@api_view(['GET'])
def get_emp(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'get_employee.html', {'employees': employees})

@api_view(['GET', 'POST'])
def update_emp_list(request):
    if request.method == 'POST':
        # Handle the form submission for updating an employee
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp_id = request.POST['employee']
            emp = get_object_or_404(Employee, id=emp_id)
            
            form = EmployeeForm(request.POST, instance=emp)
            if form.is_valid():
                form.save()
                messages.success(request, 'Employee updated successfully')
                return redirect('get_emp')
    else:
        # Retrieve the list of employees for the dropdown
        employees = Employee.objects.all()
        form = EmployeeForm()

    return render(request, 'update_employee_list.html', {'employees': employees, 'form': form})

@api_view(['GET', 'POST'])
def update_emp_form(request):
    if request.method == 'POST':
        company_id = request.POST['company_name']
        company = get_object_or_404(Company, id=company_id)
        employees = Employee.objects.filter(company_name=company)
        employee_form = EmployeeUpdateForm()
        return render(request, 'update_employee.html', {'employees': employees, 'employee_form': employee_form, 'company_id': company_id})
    else:
        employee_form = EmployeeUpdateForm()
    return render(request, 'update_employee_list.html', {'employee_form': employee_form})


@api_view(['GET', 'POST'])
def delete_employee(request):
    if request.method == 'POST':
        form = EmployeeDeleteForm(request.POST)
        if form.is_valid():
            employee_id = form.cleaned_data['employee'].id
            employee = get_object_or_404(Employee, id=employee_id)
            employee.delete()
            messages.success(request, 'Employee deleted successfully')
            return redirect('get_emp')
    else:
        form = EmployeeDeleteForm()

    return render(request, 'delete_employee.html', {'employee_form': form})

@api_view(['GET'])
def get_company_employees(request):
    companies = Company.objects.all()
    if request.method == 'GET':
        company_id = request.GET.get('company', None)
        if company_id:
            company = get_object_or_404(Company, id=company_id)
            employees = Employee.objects.filter(company_name=company)
            return render(request, 'get_company_employees.html', {'companies': companies, 'selected_company': company, 'employees': employees})
    return render(request, 'get_company_employees.html', {'companies': companies})