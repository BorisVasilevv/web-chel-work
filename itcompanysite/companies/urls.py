from . import views
from django.urls import path, include

urlpatterns = [

    path('', views.companies, name='companies'),
    path('search/', views.search, name='search')
]


