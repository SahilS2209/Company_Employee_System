from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_company/', views.add_company, name='add_company'),
    path('get_company/', views.get_company, name='get_company'),
    path('update_company_list/', views.update_company_list, name='update_company_list'),
    path('update_company_form/', views.update_company_form, name='update_company_form'),
    path('delete_company/', views.delete_company_form, name='delete_company'),
    
    path('add_emp/', views.add_emp, name='add_emp'),
    path('get_emp/', views.get_emp, name='get_emp'),
    path('update_emp_list/', views.update_emp_list, name='update_emp_list'),
    path('update_emp_form/', views.update_emp_form, name='update_emp_form'),
    path('remove_emp/', views.delete_employee, name='remove_emp'),
    
    path('get_company_employees/', views.get_company_employees, name='get_company_employees'),
]
