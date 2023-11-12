from django.shortcuts import render
from .models import Company
# Create your views here.


def napoleonit(request):
    return render(request, 'companies/napoleonit.html')


def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})

