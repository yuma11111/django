from django import forms
from django.forms import ModelForm
from .models import BookRecord

class regesterBookForm(forms.ModelForm):
    class Meta:
        model = BookRecord
        fields = ('name', 'detail','have','release_date',)
        labels={
           'name':'名前',
           'detail':'詳細',
           'have':'持っている？',
           'release_date':'発売日',
        }

        widgets = {
            'release_date': forms.NumberInput(attrs={
                "type": "date"
            })
        }