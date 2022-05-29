from django.conf.urls import path
from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^search/', views.search_results, name='search'),
    path(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
]
