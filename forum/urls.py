from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^section/(?P<section_id>\d+)/$',
        views.section_view, name="section_view"),
    url(r'^category/(?P<category_id>\d+)/$',
        views.category_view, name="category_view")
]
