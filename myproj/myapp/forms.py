from django import forms
from .models import Company, Employee


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'type']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        

class EmployeeDeleteForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Select an employee")
    
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'company_name']