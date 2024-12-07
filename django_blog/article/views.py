from django.shortcuts import render
from django.views import View


# def article(request):
#     tags = ['по дате', 'по популярности', 'по оценкам']
#     return render(
#         request,
#         'articles/index.html',
#         context={'tags': tags},
#     )

class Article(View):
    def get(self, request, *args, **kwargs):
        tags = ['по дате', 'по популярности', 'по оценкам']
        return render(
            request,
            'articles/index.html',
            context={'tags': tags},
        )