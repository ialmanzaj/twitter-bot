# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweet(models.Model):
	message = models.CharField(max_length=144)

	def __str__(self):
		return '%s' % (self.message)