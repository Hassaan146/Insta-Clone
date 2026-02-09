from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Story(models.Model):
    image = models.ImageField(upload_to='story/')
    user = models.ForeignKey(User,related_name="story_user",on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User,related_name="story_likes",blank=True)
    viewed_by = models.ManyToManyField(User,related_name="story_views",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.user.username
    