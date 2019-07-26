from django import forms
from .models import Blogs, Image, Tag

class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blogs
        
