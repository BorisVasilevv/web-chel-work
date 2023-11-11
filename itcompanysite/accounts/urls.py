from . import views
from django.urls import path, include

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('', include('django.contrib.auth.urls'))
]
