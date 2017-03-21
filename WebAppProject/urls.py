from django.conf.urls import url
from WebAppProject import views

app_name = 'workoutweb'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^account/', views.account, name='account'),
    url(r'^account_settings/', views.account_settings, name='account_settings'),
    url(r'^nearest_gym/', views.nearestgym, name='nearest_gym'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<post_name_slug>[\w\-]+)/$',
        views.show_post, name='show_post'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/(?P<post_name_slug>[\w\-]+)/liked/$',
        views.liked, name='liked'),
]
