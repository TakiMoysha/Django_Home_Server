from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full name')
    email_address = forms.EmailField(max_length=150, label='Email')
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)
