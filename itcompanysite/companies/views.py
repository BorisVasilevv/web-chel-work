from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Company, CompanyType, Favorite
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
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

@login_required
@require_POST
def add_to_favorites(request, company_id):
    company = Company.objects.get(pk=company_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, company=company)
    return JsonResponse({'status': 'added' if created else 'already_exists'})