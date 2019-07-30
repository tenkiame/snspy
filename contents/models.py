from django.db import models
from django.contrib.auth import get_user_model


class Image(models.Model):
    image = models.ImageField(upload_to='')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)

class Tag(models.Model):
    tag = models.CharField(max_length=10)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Blogs(models.Model):
    #nullを外す
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #photo = models.ManyToManyField(Image, blank=True, related_name='image')
    #thumbnail = models.ManyToManyField(Image, blank=True, related_name='thumbnail')

    def __str__(self):
        return self.title
