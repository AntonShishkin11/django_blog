from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_http_methods


# def article(request):
#     tags = ['по дате', 'по популярности', 'по оценкам']
#     return render(
#         request,
#         'articles/index.html',
#         context={'tags': tags},
#     )

# class Article(View):
#     def get(self, request, *args, **kwargs):
#         tags = ['по дате', 'по популярности', 'по оценкам']
#         return render(
#             request,
#             'articles/index.html',
#             context={'tags': tags},
#         )

class Article(View):
    def get(self, request, tags, article_id):
        response_text = f"Статья номер {article_id}. Тег {tags}"
        return HttpResponse(response_text)