from django.shortcuts import render
from . import models
from .models import Blogs, Tag, Image
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BlogAddView(CreateView, LoginRequiredMixin):
    model = Blogs
    fields = ('author', 'title', 'text', 'tag', 'photo', 'thumbnail')
    success_url = reverse_lazy('contents:bloglist')
    template_name = 'contents/blogedit.html'

class BlogListView(ListView):
    model = Blogs
    fields = ('author', 'title', 'tag', 'text', 'created_at', 'updated_at', 'photo', 'thumbnail')
    template_name = 'contents/bloglist.html'

class BlogDetailView(DetailView):
    model = Blogs
    fields = ('author', 'title', 'tag', 'text', 'created_at', 'updated_at', 'photo', 'thumbnail')
    pk_url_kwarg = 'blog_pk'
    template_name = 'contents/blogdetail.html'

class BlogEditView(UpdateView):
    model = Blogs
    fields = ('author', 'title', 'text', 'tag', 'photo', 'thumbnail')
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('contents:bloglist')
    template_name = 'contents/blogedit.html'

class BlogDeleteView(DeleteView):
    model = Blogs
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('contents:bloglist')
    template_name = 'contents/blogdelete.html'

class TagAddView(CreateView):
    model = Tag
    fields = ('tag', 'author')
    success_url = reverse_lazy('contents:taglist')
    template_name = 'contents/tagedit.html'

class TagListView(ListView):
    model = Tag
    fields = ('tag')
    template_name = 'contents/taglist.html'

class TagEditView(UpdateView):
    model = Tag
    fields = ('tag')
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('contents:taglist')
    template_name = 'contents/tagedit.html'

class TagDeleteView(DeleteView):
    model = Tag
    fields = ('tag')
    success_url = reverse_lazy('contents:taglist')
    template_name = 'contents/tagdelete.html'

class ImageAddView(CreateView):
    model = Image
    fields = ('image', 'author', 'title', 'text')
    success_url = reverse_lazy('contents:imagelist')
    template_name = 'contents/imageedit.html'

class ImageListView(ListView):
    model = Image
    fields = ('image', 'author', 'title', 'text')
    template_name = 'contents/imagelist.html'

class ImageEditView(UpdateView):
    model = Image
    fields = ('image', 'author', 'title', 'text')
    pk_url_kwarg = 'object_pk'
    success_url = reverse_lazy('contents:imageedit')
    template_name = 'contents/imageedit.html'

class ImageDeleteView(DeleteView):
    model = Image
    fields = ('image', 'author', 'title', 'text')
    success_url = reverse_lazy('contents:imagedelete')
    template_name = 'contents/imagedelete.html'
