from . import views
from django.urls import path, include

urlpatterns = [
    path('napoleonit/', views.napoleonit, name='napoleonit'),
    path('', views.companies, name='companies'),
    path('<str:category_name>/', views.companies_per_type, name='companies_per_type')
]


