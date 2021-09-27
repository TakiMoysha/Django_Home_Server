from django.contrib import admin
from django.http import request
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog.views import post_list, post, post_new

from user.views import register, profile, login_view, logout_view

urlpatterns = [
    path('', post_list, name='index'),

    path('admin/', admin.site.urls, name='admin'),

    path('post/new/', post_new, name='post_new'),
    path('post/<int:post_index>/', post, name='post_detail'),

    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
