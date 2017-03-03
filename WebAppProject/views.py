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

