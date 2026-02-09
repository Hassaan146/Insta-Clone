from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True , null=True)
    followers = models.ManyToManyField(User,related_name="user_followers",blank=True)
    following = models.ManyToManyField(User,related_name="user_following",blank=True)
    dp = models.ImageField(upload_to='images/',blank=True,null=True)
    def __str__(self):
        return self.user.username