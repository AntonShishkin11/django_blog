from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods
from .models import Article

class Article_View(View):
    def get(self, request, *args, **kwargs):
        if 'article_id' in kwargs:
            article_id = kwargs['article_id']
            response_text = f"Статья номер {article_id}."
            return HttpResponse(response_text)

        tags = ['по дате', 'по популярности', 'по оценкам']

        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'tags': tags,
                                                               'articles': articles})