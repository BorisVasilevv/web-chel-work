from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from companies.models import Company

def registration(request):

    if request.method == 'POST':
        user_reg_form = UserCreationForm(request.POST)
        if user_reg_form.is_valid():
            new_user = user_reg_form.save(commit=False)
            #Проверки
            # new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)

        context = {'user_form': user_reg_form}
        return render(request, 'account/registration.html', context)
    else:
        user_reg_form = UserCreationForm()
        context = {'user_form': user_reg_form}
        return render(request, 'account/registration.html', context)


def profile(request):
    companies = Company.objects.all()


    return render(request, 'account/profile.html', {'companies': companies})
