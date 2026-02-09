from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User,related_name="post_likes",default=0)

    def __str__(self):
        return f"Post by {self.user.username}"

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User,related_name="comments_like",blank=True)

    def __str__(self):
        return f"{self.user.username}-{self.text}"

class Feed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feed")
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")


@receiver(post_save, sender=Post)
def create_feed_entries(sender, instance, created, **kwargs):
    if created:
        followers = instance.profile.followers.all() 
        for follower in followers:
            Feed.objects.create(user=follower, posts=instance)