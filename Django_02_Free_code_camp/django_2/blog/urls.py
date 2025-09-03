
from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'blog'

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='articles'),
    path('articles/<int:id>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:id>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:id>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
