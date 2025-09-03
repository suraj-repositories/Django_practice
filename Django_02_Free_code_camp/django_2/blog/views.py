

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .form import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'  # <blog>/<model-name>_lists.html
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    # queryset = Article.objects.all()
    template_name = 'blog/article_detail.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

class ArticleUpdateView(UpdateView):
    template_name = 'blog/article_create.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    # success_url = '/'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)

    def get_success_url(self):
        return reverse('blog:articles',  kwargs={})
