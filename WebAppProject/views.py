from django.http import HttpResponse
from django.shortcuts import render
from WebAppProject.models import Category, Post, Comment
from django.core.urlresolvers import reverse
from WebAppProject.forms import PostForm, CommentForm

def index(request):
    category_list = Category.objects.order_by()[:6]
    context_dict = {}
    cat_dict = {}
    for category in category_list:
        try:
            posts = Post.objects.filter(category=category).order_by('-likes')[:5]
            cat_dict[category] = posts
        except Category.DoesNotExist:
            cat_dict[category] = None
    context_dict['categories'] = cat_dict

    return render(request,'workoutweb/index.html', context_dict)

def about(request):
    return render(request, 'workoutweb/about.html', {})

def login(request):
    return render(request, 'workoutweb/login.html', {})

def account(request):
    return render(request, 'workoutweb/account.html', {})

def nearestgym(request):
    return render(request, 'workoutweb/nearestgyum.html', {})

def contact(request):
    return render(request, 'workoutweb/contact.html', {})

def faq(request):
    return render(request, 'workoutweb/faq.html', {})

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    context_dict['repeat'] = None
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category).order_by('-likes')
        context_dict['category'] = category
        context_dict['posts'] = posts
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['posts'] = None

    try:
        category =  Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PostForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = PostForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            if category:
                try:
                    post = form.save(commit=False)
                    post.category = category
                    post.save()
                    context_dict['repeat'] = None
                except:
                    context_dict['repeat'] = 'Post title exists.'
        else:
            print(form.errors)
    context_dict['form'] = form
    return render(request, 'workoutweb/category.html', context_dict)


def show_post(request, post_name_slug, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    try:
        post = Post.objects.get(slug=post_name_slug)
        print post
        comments = Comment.objects.filter(post=post)
        context_dict['post'] = post
        context_dict['comments'] = comments
    except Post.DoesNotExist:
        context_dict['post'] = None
        context_dict['comments'] = None

    try:
        post =  Post.objects.get(slug=post_name_slug)
    except Post.DoesNotExist:
        post = None
    form = CommentForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            if post:
                comment = form.save(commit=False)
                comment.post = post
                comment.save()

    context_dict['form'] = form
    return render(request, 'workoutweb/post.html', context_dict)

