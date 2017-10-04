from django.db import models


# Create your models here.
class Community(models.Model):
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class User(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	gender = models.CharField(max_length=20, blank=True)
	profile_pic = models.CharField(max_length=500, blank=True)
	friends = models.ManyToManyField('self', blank=True)
	communities = models.ManyToManyField(Community, blank=True)

	def __str__(self):
		return self.name