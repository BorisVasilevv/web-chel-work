from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Company, Category, Subcategory, Favorite, CompanyCategory
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .helpstructure import CompanyWithFavoriteFlagAndCategoryData
from .utils import has_russian_letters


# Create your views here.

def companies(request):
    all_companies = Company.objects.all()
    result_companies = get_companies_with_favorite_flag_and_category(request, all_companies)
    subcategories = Subcategory.objects.all()
    context = {
        'subcategories': subcategories,
        'result_companies': result_companies,
    }
    return render(request, 'companies/companies.html',  context)


def companies_per_category_subcategory(request, category_or_subcategory_name):
    subcategory_list = []
    category_or_subcategory = 0
    try:
        category = Category.objects.get(Q(category_name=category_or_subcategory_name))
        category_or_subcategory = category
        subcategory_list = Subcategory.objects.filter(company_category_id=category.id)
    except ObjectDoesNotExist:
        try:
            subcategory = Subcategory.objects.get(Q(subcategory_name=category_or_subcategory_name))
            category_or_subcategory = subcategory
            subcategory_list.append(subcategory)
        except ObjectDoesNotExist:
            raise Http404

    requested_companies = []
    for subcategory in subcategory_list:
        company_categories = CompanyCategory.objects.filter(subcategory_id=subcategory.id)
        company_of_subcategory = [company_category.company for company_category in company_categories]
        requested_companies.extend(company_of_subcategory)

    result_companies = get_companies_with_favorite_flag_and_category(request, requested_companies)
    context = {
        "category_or_subcategory": category_or_subcategory,
        "result_companies": result_companies,
    }
    return render(request, 'companies/companies.html', context)


def search(request):
    query = request.GET.get("q")

    if has_russian_letters(query):
        query = query.lower()
        requested_companies_lower = Company.objects.filter(name__icontains=query)
        query = query.title()
        requested_companies_title = Company.objects.filter(name__icontains=query)
        requested_companies = requested_companies_lower.union(requested_companies_title)
    else:
        requested_companies = Company.objects.filter(name__icontains=query)

    result_companies = get_companies_with_favorite_flag_and_category(request, requested_companies)
    context = {
        "result_companies": result_companies,
    }
    return render(request, 'companies/companies.html', context)


def get_companies_with_favorite_flag_and_category(request, companies_set):
    result_comp = []
    user = request.user

    if not user.is_anonymous:
        favorite = Favorite.objects.filter(user_id=user.id)
        favorite_companies = [fav.company for fav in favorite]

        for comp in companies_set:
            is_favorite = favorite_companies.__contains__(comp)
            result_comp.append(company_to_company_with_favorite_flag_and_category_data(comp, is_favorite))

    else:
        for comp in companies_set:
            result_comp.append(company_to_company_with_favorite_flag_and_category_data(comp, False))
    return result_comp


def company_to_company_with_favorite_flag_and_category_data(company, is_favorite):
    company_categories = CompanyCategory.objects.filter(company_id=company.id)
    subcategories_by_comp = [company_categoty.subcategory for company_categoty in company_categories]
    categories_by_comp = [subcat.company_category for subcat in subcategories_by_comp]
    return CompanyWithFavoriteFlagAndCategoryData(company.id, company.name, company.logotype, company.short_description,
                                                  company.url, is_favorite, categories_by_comp, subcategories_by_comp,
                                                  company.phone, company.telegram, company.accreditation, company.email)


@login_required
@require_POST
def add_to_favorites(request, company_id):
    company = Company.objects.get(pk=company_id)
    user = request.user
    if not user.is_anonymous:
        favorite, created = Favorite.objects.get_or_create(user=request.user, company=company)
        return JsonResponse({'status': 'added' if created else 'already_exists'})


@login_required
@require_POST
def add_to_favorites_with_category(request, category_or_subcategory_name, company_id):
    company = Company.objects.get(pk=company_id)
    user = request.user
    if not user.is_anonymous:
        favorite, created = Favorite.objects.get_or_create(user=request.user, company=company)
        return JsonResponse({'status': 'added' if created else 'already_exists'})
