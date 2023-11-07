from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
# Create your views here.
def index(request):
    all_companies = Company.objects.all()
    return render(request, 'main/index.html', {'all_companies': all_companies})

def companies(request):
    return render(request, 'main/companies.html')

def napoleonit(request):
    return render(request, 'main/napoleonit.html')


