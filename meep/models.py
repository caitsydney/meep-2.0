import datetime
from django.utils import timezone
from django.db import models

class User(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()

	def __unicode__(self):
		return self.name

class Message(models.Model):
	TOPIC_CHOICES = (
		(u'HA', u'homework assignments'),
		(u'Q', u'questions'),
		(u'RS', u'random stuff'),
		(u'STS', u'shit titus says'),
		(u'SG', u'study groups'),
		(u'TT', u'tips and tricks'),
	)

	title = models.CharField(max_length=30)
	text = models.CharField(max_length=500)
	date = models.DateTimeField('date submitted')
	user = models.ForeignKey(User)
	topic = models.CharField(max_length=3, choices=TOPIC_CHOICES)
	rating = models.IntegerField()
	enable_comments = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

class Thread(models.Model):
	head = models.ForeignKey(Message)

	def __unicode__(self):
		return self.head







