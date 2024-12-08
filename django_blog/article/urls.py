from django.urls import path

from django_blog.article import views
from django_blog.article.views import Article_View

urlpatterns = [
    path("", Article_View.as_view(), name="article"),
    path("<int:article_id>/", Article_View.as_view(), name="article_view"),
]