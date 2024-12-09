from django import forms

from django_blog.article.models import *


class CommentArticleForm(forms.Form):
    content = forms.CharField(label='Комментарий')

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
        }