from django.urls import path

from django_blog.article import views
from django_blog.article.views import Article

urlpatterns = [
    path("<str:tags>/<int:article_id>/", Article.as_view(), name="article"),
]