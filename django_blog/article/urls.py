from django.urls import path

from django_blog.article import views
from django_blog.article.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="article"),
    path("<int:article_id>/", ArticleView.as_view(), name="article_view"),
    path("create/", AddArticleView.as_view(), name="add_article"),
    path('<int:id>/edit/', EditArticleView.as_view(), name='articles_update')

]