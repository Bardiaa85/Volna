from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator
from home.views import apply_profile
from home.models import Logo , FooterInfo , BrowserTabInfo
def news_page(request):
    user_full_name = apply_profile(request)
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    data = Article.objects.order_by("-article_date")
    paginator = Paginator(data , 6)
    page_number = request.GET.get("page")
    this_page = paginator.get_page(page_number)
    return render(request , "news/news.html" , {"this_page" : this_page , "active_page" : "news" , "paginator" : paginator.page_range , "user_full_name" : user_full_name , "footer_info" : footer_info , "logo" : logo , "tab_info" : tab_info})
def single_article_page(request , slug):
    user_full_name = apply_profile(request)
    logo = list(Logo.objects.all())[-1] if len(Logo.objects.all()) != 0 else None
    footer_info = list(FooterInfo.objects.all())[-1] if len(FooterInfo.objects.all()) != 0 else None
    tab_info = list(BrowserTabInfo.objects.all())[-1] if len(BrowserTabInfo.objects.all()) != 0 else None
    data = Article.objects.get(slug = slug)
    comments_list = data.comment_set.order_by("-comment_date")
    return render(request , "news/single-article.html" , {"active_page" : "news" , "article" : data , "user_full_name" : user_full_name , "comments_list" : comments_list , "footer_info" : footer_info , "logo" : logo , "tab_info" : tab_info})

    
