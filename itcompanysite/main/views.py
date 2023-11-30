from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from companies.models import Сategory, Subcategory

def index(request):
    categories = Сategory.objects.all()
    categories_with_subcategories = []
    for category in categories:
        categor = CategoryWithSubcategories(category.id,
                                            category.category_name,
                                            category.style_name,
                                            category.description)
        categor.subcategories = Subcategory.objects.filter(company_category_id=category.id)
    return render(request, 'main/index.html', {"categories": categories})

def map(request):
    return render(request, 'main/map.html')

class CategoryWithSubcategories:
    id: int
    category_name: str
    style_name: str
    description: str
    subcategories = []

    def __init__(self, categor_id, categor_name, categor_style_name, categor_description):
        self.id = categor_id
        self.category_name = categor_name,
        self.style_name = categor_style_name
        self.description = categor_description

