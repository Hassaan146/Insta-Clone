from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Story

@shared_task
def delete_expired_stories():
    expiry_time = timezone.now() - timedelta(hours=24)
    Story.objects.filter(created_at__lt=expiry_time).delete()
