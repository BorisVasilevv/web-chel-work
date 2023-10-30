from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def companies(request):
    return render(request, 'main/companies.html')

def napoleonit(request):
    return render(request, 'main/napoleonit.html')


