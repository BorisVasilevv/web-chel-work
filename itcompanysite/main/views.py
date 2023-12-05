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
                                            category.style_name,
                                            category.description)
        categor.subcategories = Subcategory.objects.filter(company_category_id=category.id)
        categories_with_subcategories.append(categor)
    return render(request, 'main/index.html', {"categories": categories_with_subcategories})

def map(request):
    return render(request, 'main/map.html')
