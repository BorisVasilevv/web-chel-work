from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('companies/', include('companies.url')),

]
