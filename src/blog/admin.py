from django.contrib import admin

from .models import File, Post

admin.site.register(Post)
admin.site.register(File)