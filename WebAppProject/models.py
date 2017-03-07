
# WHERE/ WHAT IS SLUG ?!?!?!?!?!?!?!?

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class UserProfile(models.Model):
    # links UserProfile to a user model instance
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',blank=True)

    def __str__(self):
        return self.user.username



class Category(models.Model):
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

    name = models.CharField(max_length=128, unique=True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    slug = models.SlugField(unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128, default = "")
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    content = models.CharField(max_length=1024, default = "")

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=128, default = "Comment")
    post = models.ForeignKey(Post)
    #user = models.ForeignKey(UserProfile)
    content = models.CharField(max_length=1024)
    def __str__(self):
        return self.title



