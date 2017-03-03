from django.http import HttpResponse
from django.shortcuts import render
from WebAppProject.models import Category, Post

def index(request):
    category_list = Category.objects.order_by()[:6]
    context_dict = {}
    cat_dict = {}
    for category in category_list:
        try:
            posts = Post.objects.filter(category=category)
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
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        posts = Post.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['posts'] = None
        # Go render the response and return it to the client.
    return render(request, 'workoutweb/category.html', context_dict)

