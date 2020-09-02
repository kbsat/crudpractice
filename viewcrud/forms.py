from django import forms
from .models import Blog


class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__' : 모든항목을 받을 때
        fields = ['title', 'body']
