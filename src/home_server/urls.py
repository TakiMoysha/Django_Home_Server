from django.contrib import admin
from django.http import request
from django.urls import path

from blog.views import post_list, home_view, post, post_new

from user.views import register, profile

urlpatterns = [
    path('', home_view, name='index'),

    path('admin/', admin.site.urls, name='admin'),

    path('posts/', post_list, name='posts'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_index>/', post, name='post_detail'),
    # path('register/', ...),
    # path('profile/', ...),
    path('login/', home_view, name='login'),
    path('logout/', home_view, name='logout'),
]
