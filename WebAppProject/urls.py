from django.conf.urls import url
from WebAppProject import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/login', views.login, name='login'),
    url(r'^/about', views.about, name='about'),
    url(r'^/account', views.account, name='account'),
    url(r'^/nearest-gym', views.nearestgym, name='nearest gym'),
    url(r'^/contact', views.contact, name='contact'),
    url(r'^/faq', views.faq, name='faq'),
]
