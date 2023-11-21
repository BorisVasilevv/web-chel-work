from django.shortcuts import render
from .models import Company, CompanyType
# Create your views here.


def companies(request):
    companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': companies})


def companies_per_type(request, category_name):
    cp = CompanyType.objects.get(type_name__contains=category_name)
    companies = Company.objects.filter(type_id=cp.id)
    return render(request, 'companies/companies.html',  {'companies': companies})

def search(request):
    query = request.GET.get("q")
    query = query.lower()
    companies = Company.objects.filter(name__icontains=query)
    if(companies.__len__()==0):
        query = query.title()
        companies = Company.objects.filter(name__icontains=query)


    return render(request, 'companies/companies.html', {'companies': companies})

