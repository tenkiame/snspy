from django.shortcuts import render


from . import models
from .models import Blogs
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogAddView(CreateView):
    model = Blogs
    fields = ('title', 'text', 'tag')
    success_url = reverse_lazy('contents:list')
    template_name = 'contents/blogedit.html'

class BlogListView(ListView):
    model = Blogs
    exclude = ('text',)
    template_name = 'contents/bloglist.html'
