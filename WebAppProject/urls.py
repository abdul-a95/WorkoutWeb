from django.conf.urls import url
from WebAppProject import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
