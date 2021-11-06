from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail, BadHeaderError
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse


from .forms import ContactForm, PostForm
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
    context = {}
    try:
        post = Post.objects.get(pk=primary_key)
        context['post'] = post
        return render(request, 'blog/post_details.html', context)
    except ObjectDoesNotExist as e:
        context["html_response"] = request.get_full_path()
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
    context = {'file': file}
    return render(request, 'blog/file_details.html', context)


def file_list(request):
    context = {}
    files = File.objects.filter(upload_data__lte=timezone.now()).order_by('-upload_data')
    context = {'files_list': files,}
    return render(request, 'blog/file_list.html', context)


def feedback_view(request):
    print("contact view run")
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            print("contact view valid")
            subject = "Test Messgae"
            body = {
                'full_name': contact_form.cleaned_data['full_name'],
                'email': contact_form.cleaned_data['email_address'],
                'message': contact_form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@admin.ru'])
                print("email send")
            except BadHeaderError:
                print("dab email")
                return HttpResponse('Uncorrect header')
            return redirect("index")

    print("contact view end")
    contact_form = ContactForm()
    return render(request, 'blog/feedback.html', context={'contact_form': contact_form})


@login_required
def file_new(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
        print(context)
    return render(request, 'blog/file_new.html', context)


class BaseView(View):
    """Exception Handling"""
    pass
