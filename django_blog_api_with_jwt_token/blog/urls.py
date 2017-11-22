from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.authtoken import views

from blog import views


app_name = "blog"

urlpatterns = [
    url(r'^api/auth_token/', obtain_jwt_token),
    url(r'^sign_up/', views.sign_up.as_view()),
    url(r'^login/', views.login.as_view()),
    url(r'^create_blog/', views.create_blog.as_view()),
    url(r'^list_user_blog/', views.list_user_blog.as_view()),
    url(r'^forget_password/', views.forget_password.as_view())
]