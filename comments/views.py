from django.shortcuts import render
from django.shortcuts import redirect
from .models import Comment
from releases.models import Release
from news.models import Article
def adding_comment(request , slug):
    if request.method == "POST":
        release = Release.objects.filter(slug = slug)
        article = Article.objects.filter(slug = slug)
        comment_content = request.POST.get("comment")
        if len(article) == 0 :
            release = Release.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_release = release , related_user = request.user)
            new_comment.save()
            return redirect("releases:single_release_page" , slug = slug)
        else  :
            article = Article.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user)
            new_comment.save()
            return redirect("news:single_article_page" , slug = slug)