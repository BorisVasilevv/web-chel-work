from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from companies.models import CompanyType

# Create your views here.
def index(request):
    company_types = CompanyType.objects.all()
    return render(request, 'main/index.html', {"company_types": company_types})


def map(request):

    return render(request, 'main/map.html')



