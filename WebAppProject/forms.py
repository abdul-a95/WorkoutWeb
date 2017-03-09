
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
    name = forms.CharField(label='Full Name')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(),
                                help_text="Please Enter the same password as above")
    weight = forms.IntegerField(label='Weight')
    height = forms.IntegerField(label='Height')

    class Meta:
        model = User
        fields = ('name','username','email','password','weight','height')


class UserProfileForm(forms.ModelForm):
      class Meta:
          model = UserProfile
          fields = ('picture',)

          def clean_password2(self):
              password1 = self.cleaned_data.get("password1")
              password2 = self.cleaned_data.get("password2")
              if password1 and password2 and password1 != password2:
                  raise forms.ValidationError(
                      self.error_messages['password_mismatch'],
                      code='password_mismatch',
                  )
                  self.instance.username = self.cleaned_data.get('username')
                  password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
                  return password2

          def save(self, commit=True):
              user = super.save(commit=False)
              user.set_password(self.cleaned_data["password1"])
              if commit:
                  user.save()
              return user