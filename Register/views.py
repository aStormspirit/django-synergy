from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm

from .models import Human, Profession


# Create your views here.

class RegisterView(CreateView):
    template_name = 'Human/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('Login')


def user_login(req):
    if req.method == 'POST':
        form = UserLoginForm(data=req.POST)
        if form.is_valid():
            user = form.get_user()
            login(req, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(req, 'Human/login.html', {'form': form})
