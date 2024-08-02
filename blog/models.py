from typing import Iterable
from django.db import models
from account.models import UserProfile
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(UserProfile, related_name='post_like', null=True , blank=True)
    dislike = models.ManyToManyField(UserProfile, related_name='post_dislike' , null=True , blank=True)
    slug = models.SlugField(max_length=100,null=True,blank=True)
    
    def save(self ,*args, **kwargs):
        super().save()
        if not self.slug:
            self.slug=slugify(self.title)
            self.save()
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_valid = models.BooleanField()
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    modified_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(UserProfile, related_name='comment_like' , null=True , blank=True)
    dislike = models.ManyToManyField(UserProfile, related_name='comment_dislike' , null=True , blank=True)
    slug = models.SlugField(max_length=100,null=True)
    def __str__(self):
        return f'{self.body}'
       