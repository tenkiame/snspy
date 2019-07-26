from django.shortcuts import render
from . import models
from .models import Blogs
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


class BlogAddView(CreateView):
    model = Blogs
    fields = ('author', 'title', 'text', 'tag', 'created_at', 'updated_at', 'image', 'thumbnail')
    success_url = reverse_lazy('list')
    template_name = 'contents/blogedit.html'

class BlogListView(ListView):
    model = Blogs
    fields = ('author', 'title', 'tag', 'created_at', 'updated_at', 'thumbnail')
    template_name = 'contents/bloglist.html'

class BlogDetailView(DetailView):
    model = Blogs
    fields = ('author', 'title', 'text', 'tag', 'created_at', 'updated_at', 'image', 'thumbnail')
    pk_url_kwarg = 'blog_pk'
    template_name = 'contents/blogdetail.html'

class BlogEditView(UpdateView):
    model = Blogs
    fields = ('author', 'title', 'text', 'tag', 'created_at', 'updated_at', 'image', 'thumbnail')
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('list')
    template_name = 'contents/blogedit.html'

class BlogDeleteView(DeleteView):
    model = Blogs
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('list')
    template_name = 'contents/blogdelete.html'
