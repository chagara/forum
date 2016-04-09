from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Section(models.Model):
    name = models.CharField(default='Section', max_length=32)


class Category(models.Model):
    name = models.CharField(default='Category', max_length=124)
    description = models.CharField(default='', max_length=124)
    section = models.ForeignKey(Section, default=None)


class Thread(models.Model):
    name = models.CharField(default='Thread', max_length=248)
    author = models.ForeignKey(User, default=None)
    datetime_posted = models.DateTimeField(auto_now=False, auto_now_add=False)
    category = models.ForeignKey(Category, default=None)


class Comment(models.Model):
    text = models.TextField(default=None)
    author = models.ForeignKey(User, default=None)
    datetime_posted = models.DateTimeField(default=timezone.now)
    thread = models.ForeignKey(Thread, default=None)
