from django.shortcuts import render



def article(request):
    tags = ['по дате', 'по популярности', 'по оценкам']
    return render(
        request,
        'articles/index.html',
        context={'tags': tags},
    )
