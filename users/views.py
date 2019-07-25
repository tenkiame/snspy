from django.shortcuts import render
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from . import models
from .models import Profile


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

class AccountListView(ListView):
    model = Profile
    fields = ('username', 'image')
    template_name = 'users/accountlist.html'

class ProfileView(DetailView):
    model = Profile
    fields = ('username', 'user', 'gender', 'birth', 'address', 'phone_number', 'image')
    pk_url_kwarg = 'profile_pk'
    template_name = 'users/profile.html'

class ProfileEditView(UpdateView):
    model = Profile
    fields = ('username', 'user', 'gender', 'birth', 'address', 'phone_number', 'image')
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('accountlist')
    template_name = 'profileedit.html'
