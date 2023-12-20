from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from companies.models import Category, Subcategory
from .helpstructure import CategoryWithSubcategories

def index(request):
    categories = Category.objects.all()
    categories_with_subcategories = []
    for category in categories:
        categor = CategoryWithSubcategories(category.id,
                                            category.category_name,
                                            category.color,
                                            category.description)
        categor.subcategories = Subcategory.objects.filter(company_category_id=category.id)
        categories_with_subcategories.append(categor)
    return render(request, 'main/index.html', {"categories": categories_with_subcategories})

def map(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
        "categories": categories,
        "subcategories": subcategories
    }
    return render(request, 'main/map.html', {"subcategories": subcategories})
