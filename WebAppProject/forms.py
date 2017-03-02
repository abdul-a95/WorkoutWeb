
# WHERE/ WHAT IS SLUG ?!?!?!?!?!?!?!?


from django import forms
from django.contrib.auth.models import User
from workoutweb.models import Post, Category, UserProfile


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the post.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    class Meta:
        # Provide an association between the ModelForm and a model

        model = Post  # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        fields = ('title','content',)
        # or specify the fields to include (i.e. not include the category field)
        # fields = ('title', 'url', 'views')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('name','username','email','password','weight','height')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # WTF IS website FOR ??!?!?!!?
        fields = ('website','picture')