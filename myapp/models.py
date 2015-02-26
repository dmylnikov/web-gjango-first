from django.db import models
from django import forms

class Post(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)