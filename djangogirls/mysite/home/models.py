from django.db import models
from django.utils import timezone


class Chat(models.Model):
    author = models.ForeignKey('auth.User')
    
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

