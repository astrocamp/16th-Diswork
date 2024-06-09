from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Notification
from friends.models import Friend
from chats.models import PrivateMessage
from comments.models import Comment, LikeComment
from articles.models import LikeArticle


@receiver(post_save, sender=Friend)
def handle_friend(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            title="New Friend Request",
            message=f"{instance.sender.username} 要求加你好友。",
        )


@receiver(post_save, sender=PrivateMessage)
def handle_message(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.receiver,
            title="新的訊息",
            message=f"{instance.sender.username} 傳了一則私訊。",
        )


@receiver(post_save, sender=Comment)
def handle_comment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.article.author,
            title="新的留言",
            message=f"{instance.member.username} 在你的文章底下留言。",
        )


@receiver(post_save, sender=LikeArticle)
def handle_like_article(sender, instance, created, **kwargs):
    if created:
        user = instance.article.user
        title = "新的文章按讚"
        message = f"{instance.user.username} 說你的文章讚。"

        Notification.objects.create(
            user=user,
            title=title,
            message=message,
        )


@receiver(post_save, sender=LikeComment)
def handle_like_comment(sender, instance, created, **kwargs):
    if created:
        user = instance.comment.user
        title = "新的留言按讚"
        message = f"{instance.user.username} 說你的留言讚。"

        Notification.objects.create(
            user=user,
            title=title,
            message=message,
        )
