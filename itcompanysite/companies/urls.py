from . import views
from django.urls import path, include

urlpatterns = [
    path('napoleonit/', views.napoleonit, name='napoleonit'),
    path('', views.companies, name='companies')
]


