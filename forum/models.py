from django.db import models

# Create your models here.
class Section(models.Model):
	name = models.CharField(default='Section', max_length=32)


class Category(models.Model):
	name = models.CharField(default='Category', max_length=124)
	description = models.CharField(default='', max_length=124)
	section = models.ForeignKey(Section, null=True)
