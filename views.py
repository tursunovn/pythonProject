from django.shortcuts import render
from .models import Article, Category
# Create your views here.

def index(request):
    articles = Article.objects.all()
    print(articles)
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }

    return render(request, 'blog/index.html', context)

def category_list(request, pk):
    articles = Article.objects.filter(category_id = pk)
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }

    return render(request, 'blog/index.html', context)