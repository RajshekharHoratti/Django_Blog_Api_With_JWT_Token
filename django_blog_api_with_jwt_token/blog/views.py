# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_jwt.views import obtain_jwt_token
from .models import Blog


class sign_up(APIView):
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(email)
        print(password)
        adduser = User.objects.create_user(username=username, email=email, password=password)
        outputdata = {
            "message": "Success User Has Been Created",
        }
        return JsonResponse(outputdata, safe=False)


class login(APIView):
    def post(self, request):
        data = obtain_jwt_token(request)
        renderdata = data.render()
        print(renderdata.content)
        return data


class create_blog(APIView):
    def post(self, request):
        token_userid = request.user.id
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(token_userid)
        print(title)
        print(description)
        if str(token_userid):
            blogdata = Blog(title=title, description=description, user_id=token_userid)
            blogdata.save()
            outputdata = {
                "message": "Your Blog Has Been Created"
            }
            return JsonResponse(outputdata, safe=False)
        else:
            outputdata = {
                "Error_Message": "User Id Dosent Match"
            }
            return JsonResponse(outputdata, safe=False)


class list_user_blog(APIView):
    def post(self, request):
        jsondata = []
        token_userid = request.user.id
        print(token_userid)
        if str(token_userid):
            bloglist = Blog.objects.filter(user_id=token_userid)
            if bloglist:
                for i in bloglist:
                    jsondata.append({
                        "title": i.title,
                        "description": i.description
                    })
                return JsonResponse(jsondata, safe=False)
            else:
                outputdata = {
                    "message": "No Blogs Avaliable For This User"
                }
                return JsonResponse(outputdata)
        else:
            outputdata = {
                "message": "Invalid User"
            }
            return JsonResponse(outputdata, safe=False)


class forget_password(APIView):
    def post(self, request):
        token_userid = request.user.id
        new_password = request.POST.get('new_password')
        print(token_userid)
        print(new_password)
        userdetails = User.objects.get(id=token_userid)
        userdetails.set_password(new_password)
        userdetails.save()
        print(userdetails)
        outputdata = {
            "Message": "Password Changed"
        }
        return JsonResponse(outputdata)

