from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.companies, name='companies'),
    path('search/', views.search, name='search'),
    path('<str:category_name>/', views.companies_per_type, name='companies_per_type')
]


