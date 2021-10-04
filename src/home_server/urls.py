from django.urls import path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from blog.views import post_list, post, post_new

from user.views import register, profile, login_view, logout_view

urlpatterns = [
    path('', post_list, name='index'),

    path('admin/', admin.site.urls, name='admin'),

    path('post/new/', post_new, name='post_new'),
    path('post/<int:primary_key>/', post, name='post_detail'),

    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
