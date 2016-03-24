from django.db import models

# Create your models here.
class Section(models.Model):
	name = models.CharField(default='Section', max_length=32)
