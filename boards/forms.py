from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title", "rule", "status", "picture"]
        labels = {
            "title": "看板",
            "rule": "板規",
            "status": "看板狀態",
            "picture": "看板圖片",
        }

    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "mx-1 border-2 border-gray-300 w-full"}),
    )
    rule = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "mx-1 border-2 border-gray-300 h-32 w-full"}
        ),
    )
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput,
    )
