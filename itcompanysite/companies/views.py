from django.shortcuts import render
from .models import Company, CompanyType
# Create your views here.


def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})

def companies_per_type(request, category_name):
    # if(category_name == "CustomDev"):
    #     type_id = 2
    # if (category_name == "SelfProducts"):
    #     type_id = 4
    # if (category_name == "B2G"):
    #     type_id = 3
    cp = CompanyType.objects.get(type_name__contains=category_name)
    companies = Company.objects.filter(type_id=cp.id)
    return render(request, 'companies/companies.html',  {'companies': companies})

def search(request):
    companies = Company.objects.filter(name__contains=request.GET.get("q"))
    return render(request, 'companies/companies.html', {'companies': companies})

