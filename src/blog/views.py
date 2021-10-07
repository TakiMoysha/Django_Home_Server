from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import PostForm
from .models import Post, File

def post_list(request):
    context = {}
    if request.user.is_authenticated:
        form = PostForm()
        context['form'] = form

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date'),
    context['posts_list'] = posts

    return render(request, 'blog/post_list.html', context)


def post_details(request, primary_key):
    try:
        post = Post.objects.get(pk=primary_key)
        context = {'post': post}
        return render(request, 'blog/post_details.html', context)
    except ObjectDoesNotExist as e:
        context = {"html_response": request.get_full_path()}
        return render(request, 'blog/error_not_found.html', context=context)


@login_required
def post_new(request):
    context = {}

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
        context["form"] = form

    return render(request, 'blog/post_edit.html', context)


def file_details(request, primary_key):
    file = get_object_or_404(File, pk=primary_key)
    print(file)
    context = {'file': file}
    return render(request, 'blog/file_details.html', context)


def file_list(request):
    context = {}
    files = File.objects.filter(upload_data__lte=timezone.now()).order_by('-upload_data')
    context['files_list'] = files
    return render(request, 'blog/file_list.html', context)


@login_required
def file_new(request):
    pass


class BaseView(View):
    """Exception Handling"""
    pass