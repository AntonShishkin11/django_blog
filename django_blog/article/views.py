from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.http import require_http_methods
from .models import Article


class IndexView(View):
    def get(self,request):
        tags = ['популярные', 'новые', 'высокий рейтинг']
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'tags': tags, 'articles': articles})
class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'articles/show.html', context={'article': article})
