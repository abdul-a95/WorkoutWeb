
# WHERE/ WHAT IS SLUG ?!?!?!?!?!?!?!? shhhh naji i did it x


from django import forms
from django.contrib.auth.models import User
from WebAppProject.models import Post, Category, UserProfile, Comment


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


#class UserForm(forms.ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput())

#    class Meta:
 #       model = User
  #      fields = ('name','username','email','password','weight','height')


#class UserProfileForm(forms.ModelForm):
 #   class Meta:
  #      model = UserProfile
   #     # WTF IS website FOR ??!?!?!!?
    #    fields = ('website','picture')