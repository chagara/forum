from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^section/(?P<section_id>\d+)/$',
        views.section_view, name="section_view"),
]
