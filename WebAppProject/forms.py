
# WHERE/ WHAT IS SLUG ?!?!?!?!?!?!?!? shhhh naji i did it x

import unicodedata
from django import forms
from django.contrib.auth.models import User
from WebAppProject.models import Post, Category, Comment, UserProfile


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the post.")
    content = forms.CharField(max_length=1024,
                              help_text="Please enter your post content.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #slug = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Post
        fields = ('title','content')

class CommentForm(forms.ModelForm):
        title = forms.CharField(max_length=128,
                                help_text="Please enter the title of the comment.")
        content = forms.CharField(max_length=1024,
                                    help_text="Please enter your comment.")
        class Meta:
            model = Comment
            fields = ('title', 'content')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta(object):
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('height','weight', 'picture')

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"