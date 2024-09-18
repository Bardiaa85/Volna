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
            if new_comment.content == "" :       
                return redirect("releases:single_release_page" , slug = new_comment.related_release.slug)
            new_comment.save()
            return redirect("releases:single_release_page" , slug = slug)
        else  :
            article = Article.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user)
            if new_comment.content == "" :       
                return redirect("news:single_article_page" , slug = new_comment.related_article.slug)
            new_comment.save()
            return redirect("news:single_article_page" , slug = slug)
def delete_comment(request , id):
    comment = Comment.objects.get(id = id)
    if request.user == comment.related_user or request.user.is_staff : 
        if comment.related_release :
            comment.delete()
            return redirect("releases:single_release_page" , slug = comment.related_release.slug)
        else:
            comment.delete()
            return redirect("news:single_article_page" , slug = comment.related_article.slug)
    else:
        if comment.related_release :
            return redirect("releases:single_release_page" , slug = comment.related_release.slug)
        else:
            return redirect("news:single_article_page" , slug = comment.related_article.slug)
def adding_reply(request , id):
    if request.method == "POST":
        comment = Comment.objects.get(id = id)
        comment_content = request.POST.get("comment")
        if comment.related_release != None :
            release = Release.objects.get(slug = comment.related_release.slug)
            new_comment = Comment(content = comment_content , related_release = release , related_user = request.user , replied_to = comment)
            if new_comment.content == "" :       
                return redirect("releases:single_release_page" , slug = new_comment.related_release.slug)
            new_comment.save()
            return redirect("releases:single_release_page" , slug = comment.related_release.slug)
        else  :
            article = Article.objects.get(slug = comment.related_article.slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user , replied_to = comment)
            if new_comment.content == "" :       
                return redirect("news:single_article_page" , slug = new_comment.related_article.slug)
            new_comment.save()
            return redirect("news:single_article_page" , slug = comment.related_article.slug)       
