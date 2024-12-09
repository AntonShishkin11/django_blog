from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.http import require_http_methods

from .forms import *
from .models import Article


class IndexView(View):

    def get(self,request):
        tags = ['популярные', 'новые', 'высокий рейтинг']
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'tags': tags, 'articles': articles})

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'articles/show.html', context={'article': article, 'form': form})

class AddArticleView(View):

    def get(self, request, *args, **kwargs):
        form = CreateArticleForm()
        return render(request, 'articles/add_article.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_view', article_id=Article.objects.last().pk)

        return render(request, 'articles/add_article.html', {'form': form})


# class CommentArticleView(View):
#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm() # Создаем экземпляр формы
#         return render(request, 'show.html', {'form': form}) # Передаем форму в контексте
