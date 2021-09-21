from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from .forms import PostForm
from .models import Post

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


def post(request):
    post = Post.objects.get()
    context = {
        'post': post
    }
    return render(request, 'blog/post_details.html', context)


@login_required
def post_new(request):
    context = {}

    if request.method == "POST":
        pass
    else:
        form = PostForm()
        context["form"] = form

    return render(request, 'blog/post_edit.html', context)


def home_view(request):
    return render(request, 'blog/home.html', {})