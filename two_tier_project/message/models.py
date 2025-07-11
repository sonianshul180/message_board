# models.py

from django.db import models
from django.utils import timezone

class Message(models.Model):
    sender = models.CharField(max_length=50)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.sender}: {self.content[:30]}"




