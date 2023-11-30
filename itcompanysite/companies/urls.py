from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.companies, name='companies'),
    path('search/', views.search, name='search'),
    path('<str:category_name>/', views.companies_per_category, name='companies_per_category'),
    path('<str:subcategory_name>/', views.companies_per_subcategory, name='companies_per_subcategory'),
    path('add_to_favorites/<int:company_id>/', views.add_to_favorites, name='add_to_favorites')
]


