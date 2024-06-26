from django.db import models
from django.utils import timezone
from boards.models import Category
from lib.softdelete import SoftDeleteable


class Event(SoftDeleteable, models.Model):
    summary = models.CharField(max_length=100, default="")
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    description = models.TextField(default="")
    deleted_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, default=1
    )
