from django.urls import path

from django_blog.article import views
from django_blog.article.views import Article

urlpatterns = [
    path("", Article.as_view(), name="articles"),
]