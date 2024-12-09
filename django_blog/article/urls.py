from django.urls import path

from django_blog.article import views
from django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    path("", IndexView.as_view(), name="article"),
    path("<int:article_id>/", ArticleView.as_view(), name="article_view"),
]