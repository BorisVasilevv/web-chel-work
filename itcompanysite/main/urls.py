from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('companies/', views.companies, name='companies'),
    path('companies/napoleonit', views.napoleonit, name='napoleonit')
]
