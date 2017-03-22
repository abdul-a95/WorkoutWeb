import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'workoutweb.settings')

import django
django.setup()
from random import randint
import datetime

from WebAppProject.models import Category, Post, Comment

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    supplements_posts = [
        {"title":"New protein",
         "content":"Found a new protein powder you guys should try",
         "likes": 9,
         "views": 19,
         },
        {"title": "Effects of steroids",
         "content": "For anyone thinking about taking steroids. Here is some information about the effects it can have on your body and how they can impact your life mentally too.",
         "likes": 98,
         "views": 138,
         }
    ]
    equipment_posts = [
        {"title": "The best equipment for starters",
         "content": "Hey everyone, I was browsing online and found a good cheap brand of equipment. They've got something for everyone. Check it out at ...",
         "likes": 41,
         "views": 76,
         }
    ]
    programs_posts = [
        {"title": "Ab Workout",
         "content": "Summer's coming up soon and everyone wants their six packs! Here's a great workout that i put together. It begins with ...",
         "likes": 7,
         "views": 18,
         }
    ]
    exercises_posts = [
        {"title": "Exercises you can do at home",
         "content": "I put together a list of things you can work on while you're at home. Feel free to use these workouts to create your own program!",
         "likes": 281,
         "views": 502,
         },
        {"title": "A list of chest workouts",
         "content": "Here is a list of workouts you can do to build a chest like Arnold himself: ...",
         "likes": 8977,
         "views": 12949,
         }
    ]
    nutrition_posts = [
        {"title": "Carb loading",
         "content": "If you're looking to bulk i put some recipes together to help you along the way. These will bring some variety to your usual meals...",
         "likes": 485,
         "views": 1299,
         }
    ]
    other_posts = [
        {"title": "Introducing myself",
         "content": "Hey guys I'm John Smith, im new to the site and just wanted to get to know people on here. I'm 24 years old and trying to get serious with my gym life",
         "likes": 49,
         "views": 90,
         },
        {"title": "Need some help!",
         "content": "I'm having problems staying motivated for the gym. I'm not seeing a big change in my weight and gym takes a lot of time...",
         "likes": 49,
         "views": 90,
         },
        {"title": "Check these gainzzzz!",
         "content": "Here are my before and after pictures after 3 years in the gym. Hit me up with some feedback!!!!! ...",
         "likes": 49,
         "views": 90,
         }
    ]

    comment = {"Comment1": "Nice post friend!", "Comment2": "Hey this post really helped me out thanks"}
    cats = {"Supplements": {"posts": supplements_posts},
            "Workout Equipment": {"posts": equipment_posts},
            "Workout Programs": {"posts": programs_posts},
            "Exercises": {"posts": exercises_posts},
            "Nutrition": {"posts": nutrition_posts},
            "Other": {"posts": other_posts}}

      # If you want to add more catergories or pages,
      # add them to the dictionaries above.

      # The code below goes through the cats dictionary, then adds each category,
      # and then adds all the associated pages for that category.
      # if you are using Python 2.x then use cats.iteritems() see
      # http://docs.quantifiedcode.com/python-anti-patterns/readability/
      # for more information about how to iterate over a dictionary properly.


    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["posts"]:
            add_post(c, p["title"],comment, p["content"], p["likes"], p["views"])

      # Print out the categories we have added.

    for c in Category.objects.all():
            for p in Post.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))




def add_post(cat, title, comments,  content, likes=0, views=0):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.likes = likes
    p.views = views
    p.content = content
    p.user = "John Smith"
    now = datetime.datetime.now()
    p.time = now.strftime('%B ''%d'', ''%Y '' at ''%I'':''%M'' %p')
    p.save()
    for comment in comments:
        c = Comment.objects.get_or_create(post = p, title = comment)[0]
        c.content = comments[comment]
        c.time = now.strftime('%B ''%d'', ''%Y '' at ''%I'':''%M'' %p')
        c.username = "Guest"+str((randint(0,1000)))
        c.save()
    return p

def add_cat(name):
     c = Category.objects.get_or_create(name=name)[0]
     c.save()
     return c

      # Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
