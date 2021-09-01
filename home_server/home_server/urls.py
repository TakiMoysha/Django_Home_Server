from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ...),
    path('register/', ...),
    path('profile/', ...),
    path('logout/', ...),
    path('', ...),
]
