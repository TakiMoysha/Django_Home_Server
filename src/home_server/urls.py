from django.urls import path, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from blog.views import file_details, file_list, file_new, post_list, post_details, post_new, feedback_view

from user.views import register, profile, my_profile, login_view, logout_view

urlpatterns = [
    path('', post_list, name='index'),
    path('', post_list, name='homepage'),

    path('admin/', admin.site.urls, name='admin'),

    path('post/new/', post_new, name='post_new'),
    path('post/<int:primary_key>/', post_details, name='post_detail'),

    path('files/', file_list, name='files'),
    path('file/new/', file_new, name='file_new'),
    path('file/<int:primary_key>/', file_details, name='file_details'),

    path('profile/', my_profile, name='my_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', profile, name='profile'),
    path('register/', register, name='register'),

    path('feedback/', feedback_view, name='feedback'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)),]
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
