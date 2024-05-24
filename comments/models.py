from django.db import models
from django.utils import timezone
from django.conf import settings
from martor.models import MartorField

class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)
    
class Comment(models.Model):
    member = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    content = MartorField() 
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
    like_comment = models.ManyToManyField(settings.AUTH_USER_MODEL, through="LikeComment", related_name="like_comment")
    
    objects = CommentManager()
    
    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        
class LikeComment(models.Model):
    like_comment = models.ForeignKey("Comment", related_name="comment", on_delete=models.CASCADE)
    like_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sender", on_delete=models.CASCADE)