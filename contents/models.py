from django.db import models

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#   author、image、thumbnailを追加
