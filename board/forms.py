from django import forms
from django.core.exceptions import ValidationError
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
       model = Post
       fields = [
           'title',
           'category',
           'text',
           'author'
       ]
       widgets = {
           'title': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 3}),
           'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 70, 'rows': 10}),
       }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Категория:"
        self.fields['title'].label = "Название"
        self.fields['text'].label = "Текст:" 

    def clean_name(self):
        name = self.cleaned_data["title"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name
    
    def clean_text(self):
        name = self.cleaned_data["text"]
        if name[0].islower():
            raise ValidationError(
                "Текст должен начинаться с заглавной буквы"
            )
        return name