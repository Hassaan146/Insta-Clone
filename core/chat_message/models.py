from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    msg = models.TextField()
    sender = models.ForeignKey(User,related_name="message_sender",on_delete=models.CASCADE)
    receiver = models.ForeignKey(User,related_name="message_receiver",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.msg
    

class Group(models.Model):
    name = models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to='image/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    members = models.ManyToManyField(User,related_name="group_members")
    admin = models.ForeignKey(User,related_name="group_admin",on_delete=models.SET_NULL, null=True, blank=True)
    messages = models.ManyToManyField(Message,related_name="group_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
