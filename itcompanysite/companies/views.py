from django.shortcuts import render
from .models import Company
# Create your views here.


def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})


def search(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})

