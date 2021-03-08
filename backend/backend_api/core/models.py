import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    content = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos'
    )
