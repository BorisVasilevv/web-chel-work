from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def login( request):
    return render(request, 'main/login.html')

def registration (request):
    if request.method == 'POST':
        user_reg_form = UserRegistrationForm(request.POST)
        if user_reg_form.is_valid():
            new_user = user_reg_form.save(commit=False)
            #Проверки
            # new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'main/index.html', {'new_user': new_user})
        user_reg_form = UserRegistrationForm()
        return render(request, 'main/registration.html', {'user_form': user_reg_form})
    else:
        user_reg_form = UserRegistrationForm()
        return render(request, 'main/registration.html', {'user_form': user_reg_form})


