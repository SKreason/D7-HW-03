from django.urls import path
from .views import (NewsList, PostDetail, PostSearch, NewCreate, PublicationsList, ArticlesList, ArticleCreate,
                    PostEdit, PostDelete, subscriptions)

urlpatterns = [
    path('', PublicationsList.as_view(), name='publication'),
    path('news/', NewsList.as_view(), name='news'),
    path('articles/', ArticlesList.as_view(), name='articles'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search', PostSearch.as_view()),
    path('news/create/', NewCreate.as_view(), name='news.add_post'),
    path('articles/create/', ArticleCreate.as_view(), name='article.add_post'),
    path('news/<int:pk>/edit', PostEdit.as_view()),
    path('articles/<int:pk>/edit', PostEdit.as_view()),
    path('news/<int:pk>/delete', PostDelete.as_view()),
    path('articles/<int:pk>/delete', PostDelete.as_view()),
    path('subscriptions/', subscriptions, name='subscriptions'),
]
