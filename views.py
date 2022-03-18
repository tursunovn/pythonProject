from django.shortcuts import render, redirect
from .models import Article, Category
# Create your views here.
from .forms import ArticleForm
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


def index(request):
    articles = Article.objects.all()
    print(articles)
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }

    return render(request, 'blog/all_articles.html', context)


def category_list(request, pk):
    articles = Article.objects.filter(category_id=pk)
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }

    return render(request, 'blog/all_articles.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'title': article.title,
        'article': article
    }

    return render(request, 'blog/article_detail.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            return redirect('article_detail', article.pk)


    else:
        form = ArticleForm()

    context = {
        'title': 'Добавить статью',
        'form': form
    }

    return render(request, 'blog/article_form.html', context)

class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'blog/all_articles.html'
    extra_context = {
        'title': 'Главная страница из классов'
    }

    def get_queryset(self):
        return Article.objects.filter(is_published = True)

class ArticleListByCategory(ArticleList):
    def get_queryset(self):
        return Article.objects.filter(
            category_id=self.kwargs['pk'], is_published = True
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Категория: {category.title}'
        return context

class ArticleDetail(DetailView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'], is_published =True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Статья: {article.title}'
        articles = Article.objects.all()
        context['articles'] = articles.order_by('created_at')[:4]
        return context



class NewArticle(CreateView):
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    extra_context = {
        'title': 'Добавить статью'
    }

class SearchResults(ArticleList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(title__icontains=word)
        return articles

class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
