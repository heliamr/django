from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.


class UserProfile(models.Model):
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_picture" , default="user-account.jpg")
    def __str__(self):
        return f'{self.user.username}'
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    

class Education(models.Model):
    school = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    fromDate = models.DateTimeField(auto_now_add=True)
    toDate = models.DateTimeField()
    description = models.DateTimeField()
    
class Experience(models.Model):
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    fromDate = models.DateTimeField(auto_now_add=True)
    toDate = models.DateTimeField()
    description = models.DateTimeField()
    
@receiver(post_save, sender=User)
def _create_userprofile(sender,instance, **kwargs):
    if UserProfile.objects.filter(user=instance).count()==0:
        UserProfile.objects.create(user=instance)