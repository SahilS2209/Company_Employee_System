from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + ' - ' + str(self.company_name)