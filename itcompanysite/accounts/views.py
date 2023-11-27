from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import login
from companies.models import Company
from django.utils.http import urlsafe_base64_decode
from django.views import View
from .forms import MyUserCreationForm, MyAuthenticationForm
from .utils import send_email_for_verify
from django.contrib.auth.tokens import default_token_generator as token_generator


User = get_user_model()
def registration(request):
    if request.method == 'POST':
        user_reg_form = MyUserCreationForm(request.POST)
        if user_reg_form.is_valid():
            new_user = user_reg_form.save()
            #Проверки
            # new_user.set_password(user_form.cleaned_data['password'])

            send_email_for_verify(request, new_user)
            return redirect('/accounts/confirm_email/')
            # login(request, new_user)
            # return redirect('/accounts/profile/')
        context = {'user_form': user_reg_form}
        return render(request, 'accounts/registration.html', context)
    else:
        user_reg_form = MyUserCreationForm()
        context = {'user_form': user_reg_form}
        return render(request, 'accounts/registration.html', context)


def profile(request):
    companies = Company.objects.all()
    return render(request, 'accounts/profile.html', {'companies': companies})

class EmailView(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('profile')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user

class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = MyAuthenticationForm




