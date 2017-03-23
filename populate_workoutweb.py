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
         },
        {"title": "Creatine",
         "content": "Just started using this new creatine powder called creapure, highly recommended.",
         "likes": 100,
         "views": 200,
         },
        {"title": "Mass Gainer",
         "content": "My Protein have a sale on mass gainer, really cheap",
         "likes": 50,
         "views": 120,
         },
        {"title": "Pre-Workout",
         "content": "mango and pineapple pre-workout available here...",
         "likes": 62,
         "views": 180,
         },
        {"title": "Pre-Workout effects",
         "content": "I want to start taking pre-workout when working out but unsure of the effects, can someone help pls",
         "likes": 69,
         "views": 500,
         },
        {"title": "Milk protein powder",
         "content": "Started using this new protein powder from bodybuilding.com",
         "likes": 89,
         "views": 190,
         }

    ]
    equipment_posts = [
        {"title": "The best equipment for starters",
         "content": "Hey everyone, I was browsing online and found a good cheap brand of equipment. They've got something for everyone. Check it out at ...",
         "likes": 41,
         "views": 76,
         },
        {"title": "Dumbells over barbells",
         "content": "Hey guys, not sure whether dumbells or the barbell is better to build a bigger chest, any suggestions?",
         "likes": 56,
         "views": 100,
         },
        {"title": "What is the best equipment",
         "content": "What is the best equipment",
         "likes": 2,
         "views": 10,
         },
        {"title": "Gym equipment for sale",
         "content": "Hey peeps, i'm selling a set of 10kg dumbells, let me know if interested",
         "likes": 120,
         "views": 250,
         },
        {"title": "broken barbell",
         "content": "Broke my barbell, any chance to get it fixed?",
         "likes": 56,
         "views": 120,
         },
        {"title": "Gym gloves",
         "content": "Got a pair of workout gloves if anyone wants them, only been used once",
         "likes": 36,
         "views": 100,
         }

    ]
    programs_posts = [
        {"title": "Ab Workout",
         "content": "Summer's coming up soon and everyone wants their six packs! Here's a great workout that i put together. It begins with ...",
         "likes": 7,
         "views": 18,
         },
        {"title": "Chest Workout",
         "content": "Here is my chest workout: 5 sets dumbell press, 3 sets dumbell flies",
         "likes": 20,
         "views": 60,
         },
        {"title": "What is a good workout",
         "content": "Hey guys, what is a good workout when bulking",
         "likes": 70,
         "views": 125,
         },
        {"title": "Back Workout",
         "content": "Hey, what is a good back workout plan?",
         "likes": 7,
         "views": 56,
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
         },
        {"title": "Ab exercises",
         "content": "Trying to define my abs, what are the best exercises?",
         "likes": 1000,
         "views": 1320,
         },
        {"title": "Workouts at home",
         "content": "Can't afford the gym so can anyone recommend any good home workouts",
         "likes": 125,
         "views": 300,
         },
        {"title": "A list of shoulder workouts",
         "content": "Here is a list of workouts you can do to have big boulder shoulders like Arnold himself: ...",
         "likes": 9000,
         "views": 10000,
         },
        {"title": "leg exercises for females",
         "content": "What are the best leg workouts for females, i've just recently joined the gym",
         "likes": 1255,
         "views": 3000,
         }
    ]
    nutrition_posts = [
        {"title": "Carb loading",
         "content": "If you're looking to bulk i put some recipes together to help you along the way. These will bring some variety to your usual meals...",
         "likes": 485,
         "views": 1299,
         },
        {"title": "Smoking is bad",
         "content": "Smoking is bad for health, no way right?",
         "likes": 1256,
         "views": 4000,
         },
        {"title": "How to cut for summer",
         "content": "What is the best diet plan to cut for summer?",
         "likes": 1456,
         "views": 3560,
         },
        {"title": "Benefits of eating fruit",
         "content": "There are so many fruits out there which are good for health, here are some...",
         "likes": 14555,
         "views": 50000,
         }
    ]
    other_posts = [
        {"title": "Introducing myself",
         "content": "Hey guys I'm John Smith, im new to the site and just wanted to get to know people on here. I'm 24 years old and trying to get serious with my gym life",
         "likes": 560,
         "views": 1400,
         },
        {"title": "Need some help!",
         "content": "I'm having problems staying motivated for the gym. I'm not seeing a big change in my weight and gym takes a lot of time...",
         "likes": 100,
         "views": 250,
         },
        {"title": "Check these gainzzzz!",
         "content": "Here are my before and after pictures after 3 years in the gym. Hit me up with some feedback!!!!! ...",
         "likes": 1256,
         "views": 1456,
         },
        {"title": "WASSUP GUYS",
         "content": "Hey guys, just new to this, would love to hear everyone's views",
         "likes": 50,
         "views": 90,
         },
        {"title": "Let's do this!",
         "content": "hey, what you upto guys",
         "likes": 12,
         "views": 50,
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
