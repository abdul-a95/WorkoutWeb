from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

# category model that contains a name as a field
# and a sluf field
class Category(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

# Post model that takes all the fields defined below
# and contains a slug field
# has relationships with category and userprofile model
class Post(models.Model):
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, default = "")
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    content = models.CharField(max_length=1024, default = "")
    user = models.CharField(max_length=128, default="John Smith")
    userliked = models.ManyToManyField(User)
    time = models.CharField(default='', max_length=128)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

# Comment model which takes all the fields defined below
# and contains relationships with post and userprofile model
class Comment(models.Model):
    title = models.CharField(default = "Comment", max_length = 128)
    time = models.CharField(default = '', max_length=128)
    post = models.ForeignKey(Post,related_name='comments')
    user = models.ForeignKey(User,null=True)
    content = models.CharField(max_length=1024)
    username = models.CharField(default="Guest", max_length=128)

    def __str__(self):
        return self.title

#Userprofile model that takes all the fields defined below
class UserProfile(models.Model):
    # links UserProfile to a user model instance
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    height = models.IntegerField(default=0,blank=True,null=True,validators=[MinValueValidator(0)])
    weight = models.IntegerField(default=0,blank=True,null=True,validators=[MinValueValidator(0)])
    picture = models.ImageField(upload_to='profile_images',blank=True)
    bio = models.CharField(max_length=250, default="hey there")


    def __str__(self):
        return self.user.username

