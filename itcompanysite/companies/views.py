from django.shortcuts import render

# Create your views here.


def napoleonit(request):
    return render(request, 'companies/napoleonit.html')


def companies(request):
    return render(request, 'companies/companies.html')