import json
from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Comment
from releases.models import Release
from news.models import Article
def adding_comment(request , slug):
    if request.method == "POST":
        release = Release.objects.filter(slug = slug)
        article = Article.objects.filter(slug = slug)
        json_data = json.loads(request.body)
        comment_content = json_data.get("content" , "")
        if len(article) == 0 :
            release = Release.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_release = release , related_user = request.user)
            if new_comment.content == "" :       
                return JsonResponse({"has_content" : False , "status" : "success" , "message" : "Data saved successfully"})
            new_comment.save()
            json_comment = model_to_dict(new_comment)
            return JsonResponse({"has_content" : True , "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully" , "allowed_to_del" : request.user == new_comment.related_user or request.user.is_staff})
        else  :
            article = Article.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user)
            if new_comment.content == "" :       
                return JsonResponse({"has_content" : False , "status" : "success" , "message" : "Data saved successfully"})
            new_comment.save()
            json_comment = model_to_dict(new_comment)
            return JsonResponse({"has_content" : True , "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully" , "allowed_to_del" : request.user == new_comment.related_user or request.user.is_staff})
def delete_comment(request , id):
    comment = Comment.objects.get(id = id)
    if request.user == comment.related_user or request.user.is_staff : 
        if comment.related_release :
            comment.delete()
            data = {"status" : "success" , "message" : "Data saved successfully"}
            return JsonResponse(data)
        else:
            comment.delete()
            data = {"status" : "success" , "message" : "Data saved successfully"}
            return JsonResponse(data)
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
