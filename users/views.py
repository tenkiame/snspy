from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from . import models
from .models import Profile
from .forms import ProfileFormset


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        ctx = super(SignUpView, self).get_context_data(**kwargs)
        ctx.update(dict(formset=ProfileFormset(self.request.POST or None, instance=self.object)))
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        formset = ctx['formset']
        if formset.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
            formset.save()
            return redirect(self.success_url())
        else:
            ctx['form'] = form
            return self.render_to_response(ctx)

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
