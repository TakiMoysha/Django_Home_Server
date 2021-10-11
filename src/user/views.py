from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user.models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleand_data.get('username')
            messages.success(request, f'Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# # profile view with flag (one view for my_profile and profile)
# def profile(request, username):
#     try:
#         user = Profile.objects.get(username=request.user)
#     except Exception as err:
#         raise Http404
#     editable = False
#     if request.user.is_authenticated() and request.user == user:
#         editable = True

#     context = locals()
#     return render(request, 'users/profile.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    # user = Profile.objects.get(username)
    context = {"user": user}
    return render(request, 'users/profile.html', context)


@login_required
def my_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Account update')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }
    return render(request, 'users/profile.html', context)


def login_view(request):
    return auth_views.LoginView.as_view(template_name='users/login.html')


def logout_view(request):
    view = auth_views.LogoutView.as_view(template_name='users/logout.html')
    context = {
        login_view: login_view
    }
    return auth_views.LogoutView.as_view(template_name='users/logout.html')

