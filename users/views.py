from django.shortcuts import render
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class Accounts(ListView):
    model = get_user_model()
    fields = ('username', 'email')
    template_name = 'users/accounts.html'
