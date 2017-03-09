from django import template
from WebAppProject.models import Category

register = template.Library()

@register.inclusion_tag('workoutweb/cats.html')
def get_category_list(cat=None):
    return {'cats': Category.objects.all(),'act_cat':cat}