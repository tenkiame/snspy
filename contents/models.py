from django.db import models
from django.contrib.auth import get_user_model

class Blogs(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    # manytomany
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ForeignKey(Image, on_delete=models.CASCADE, blank=True, related_name='image')
    thumbnail = ForeignKey(Image, on_delete=models.CASCADE, blank=True, related_name='thumbnail')

class Image(models.Model):
    image = models.ImageField(upload_to='')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

class Tag(models.Model):
    tag = models.CharField(max_length=10)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
