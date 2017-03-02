import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'workoutweb.settings')

import django
django.setup()

from WebAppProject.models import Category, Post

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    supplements_posts = []
    equipment_posts = []
    programs_posts = []
    exercises_posts = []
    nutrition_posts = []
    other_posts = []

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
            add_post(c, p["title"],p["content"], p["likes"], p["views"])

      # Print out the categories we have added.

    for c in Category.objects.all():
            for p in Post.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))



def add_post(cat, title, content, likes=0, views=0):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.likes = likes
    p.views = views
    p.content = content
    p.save()
    return p

def add_cat(name):
     c = Category.objects.get_or_create(name=name)[0]
     c.save()
     return c

      # Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
