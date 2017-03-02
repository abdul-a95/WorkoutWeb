from django.http import HttpResponse
from django.shortcuts import render
from WebAppProject.models import Category

def index(request):
    category_list = Category.objects.order_by()[:6]
    context_dict = {'categories': category_list}
    print "Help ",category_list
    return render(request,'workoutweb/index.html', context_dict)

def about(request):
    return render(request, 'workout/about.html', {})

def login(request):
    return render(request, 'workout/login.html', {})

def account(request):
    return render(request, 'workout/account.html', {})

def nearestgym(request):
    return render(request, 'workout/nearestgyum.html', {})

def contact(request):
    return render(request, 'workout/contact.html', {})

def faq(request):
    return render(request, 'workout/faq.html', {})

