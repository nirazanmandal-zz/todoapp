from django import forms
from .models import Category, TodoList


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
    }


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = [
            'title',
            'content',
            'category',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
