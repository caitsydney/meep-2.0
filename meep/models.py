from datetime import datetime
from django.utils import timezone
from django.db import models
from django import forms
from django.contrib.auth.models import User

class Thread(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField('date submitted')
	creator = models.ForeignKey(User, blank=True, null=True)
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return ('meep:topic', [self.id])
	
	def head(self):
		try:
			return self.posts.select_related().order_by('created')[0]
		except IndexError:
			return None
		
	def posts(self):
		return Message.objects.filter(thread_id=self.id).select_related()
	
class Message(models.Model):
	title = models.CharField(max_length=60)
	body = models.CharField(max_length=1000)
	created = models.DateTimeField('date submitted')
	creator = models.ForeignKey(User, blank=True, null=True)
	thread = models.ForeignKey(Thread)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return('meep:message', [self.id])

