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
            return JsonResponse({"has_content" : True , "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully"})
        else  :
            article = Article.objects.get(slug = slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user)
            if new_comment.content == "" :       
                return JsonResponse({"has_content" : False , "status" : "success" , "message" : "Data saved successfully"})
            new_comment.save()
            json_comment = model_to_dict(new_comment)
            return JsonResponse({"has_content" : True , "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully"})
def delete_comment(request , id):
    comment = Comment.objects.get(id = id)
    len_replies = len(tuple(comment.replies.all()))
    is_a_reply = comment.replied_to != None
    if request.user == comment.related_user or request.user.is_staff : 
        if comment.related_release :
            comment.delete()
            data = {"status" : "success" , "message" : "Data saved successfully" , "len_replies" : len_replies , "is_a_reply" : is_a_reply}
            return JsonResponse(data)
        else:
            comment.delete()
            data = {"status" : "success" , "message" : "Data saved successfully" , "len_replies" : len_replies , "is_a_reply" : is_a_reply}
            return JsonResponse(data)
    else:
        if comment.related_release :
            return redirect("releases:single_release_page" , slug = comment.related_release.slug)
        else:
            return redirect("news:single_article_page" , slug = comment.related_article.slug)
def adding_reply(request , id):
    if request.method == "POST":
        comment = Comment.objects.get(id = id)
        json_data = json.loads(request.body)
        comment_content = json_data.get("content" , "")
        if comment.related_release != None :
            release = Release.objects.get(slug = comment.related_release.slug)
            new_comment = Comment(content = comment_content , related_release = release , related_user = request.user , replied_to = comment)
            if new_comment.content == "" :       
                return JsonResponse({"has_content" : False , "status" : "success" , "message" : "Data saved successfully"})
            new_comment.save()
            replied_to_json = model_to_dict(new_comment.replied_to)
            json_comment = model_to_dict(new_comment)
            return JsonResponse({"has_content" : True , "replied_to_json" : replied_to_json  , "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully"})
        else  :
            article = Article.objects.get(slug = comment.related_article.slug)
            new_comment = Comment(content = comment_content , related_article = article , related_user = request.user , replied_to = comment)
            if new_comment.content == "" :       
                return JsonResponse({"has_content" : False , "status" : "success" , "message" : "Data saved successfully"})
            new_comment.save()
            replied_to_json = model_to_dict(new_comment.replied_to)
            json_comment = model_to_dict(new_comment)
            return JsonResponse({"has_content" : True ,"replied_to_json" : replied_to_json  ,  "comment" : json_comment , "is_comment_user_admin" : new_comment.related_user.is_staff , "comment_user_name" : new_comment.related_profile().full_name , "comment_time" : new_comment.get_time() , "comment_date" : new_comment.get_solar_date() , "status" : "success" , "message" : "Data saved successfully"})    
