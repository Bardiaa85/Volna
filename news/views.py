from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator
def news_page(request):
    data = Article.objects.order_by("-article_date")
    paginator = Paginator(data , 6)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "news/news.html" , {"this_page" : this_page , "active_page" : "news" , "paginator" : paginator.page_range})
def single_article_page(request , slug):
    data = Article.objects.get(slug = slug)
    return render(request , "news/single-article.html" , {"active_page" : "news" , "article" : data})

    
