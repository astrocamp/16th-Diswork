from django import forms
from martor.fields import MartorFormField
from .models import Comment

class CommentForm(forms.ModelForm):
    content = MartorFormField()
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content":"留言內容",
        }