from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')




