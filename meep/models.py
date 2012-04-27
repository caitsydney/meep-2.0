import datetime
from django.utils import timezone
from django.db import models
from django import forms
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=60)
	body = models.CharField(max_length=500)
	created = models.DateTimeField('date submitted', auto_now_add=True)
	creator = models.ForeignKey(User, related_name='posts', blank=True, null=True)
	parent = models.ForeignKey('self', null=True, blank=True, related_name='child')
	url = forms.URLField()
	thread = models.ForeignKey(Thread, related_name="posts")
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return('meep:message', [self.id])

class Thread(models.Model):
	title = models.CharField(max_length=60)
	created = models.DateTimeField('date submitted', auto_now_added=True)
	absolute_url(forms.URLField(label='absolute path', required=True)
	url = forms.URLField()	
	
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