from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Company, Category, Subcategory, Favorite, CompanyCategory
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# Create your views here.


def companies(request):
    all_companies = Company.objects.all()
    return render(request, 'companies/companies.html', {'companies': all_companies})


def companies_per_category(request, category_name):
    company_category = Category.objects.get(category_name__contains=category_name)

    company_categories = CompanyCategory.objects.filter(category_id=company_category.id)
    companies_some_category = [comp_category.company_id for comp_category in company_categories]
    return render(request, 'companies/companies.html', {'companies': companies_some_category})


def companies_per_subcategory(request, subcategory_name):
    company_subcategory = Subcategory.objects.get(subcategory_name__contains=subcategory_name)
    company_categories = CompanyCategory.objects.filter(subcategory_id=company_subcategory.id)
    companies_some_subcategory = [comp_subcategory.company_id for comp_subcategory in company_categories]
    return render(request, 'companies/companies.html', {'companies': companies_some_subcategory})


def search(request):
    query = request.GET.get("q")
    query = query.lower()
    result_companies = Company.objects.filter(name__icontains=query)
    if result_companies.__len__() == 0:
        query = query.title()
        result_companies = Company.objects.filter(name__icontains=query)
    return render(request, 'companies/companies.html', {'companies': result_companies})


@login_required
@require_POST
def add_to_favorites(request, company_id):
    company = Company.objects.get(pk=company_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, company=company)
    return JsonResponse({'status': 'added' if created else 'already_exists'})
