from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^section/(?P<pk>\d+)/$',
        views.section_view, name="section_view"),
    url(r'^category/(?P<pk>\d+)/$',
        views.category_view, name="category_view"),
    url(r'^thread/(?P<pk>\d+)/$', views.thread_view, name="thread_view")
]
