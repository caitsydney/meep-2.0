from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from meep.models import Message, User, Thread
from django import forms
import sqlite3

conn = sqlite3.connect('meep.db')
cursor = conn.cursor()

### ACTION ###
#displays index page#
def index(request):
	print "enter index"
	return render_to_response('meep/index.html')

### ACTION ###
#adds a new user#
def add_user(request):
	#initialize variables to send to template
	form = add_user_form(auto_id=True)

	if request.method == 'POST': #if the form is submitted
		form = add_user_form(request.POST) 
		if form.is_valid(): #if validation rules pass
			#username = Context.POST['username']
			#password = Context.POST['password']
			username = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			cursor.execute('INSERT INTO User VALUES (' + username + ', ' + pw + ')')
			return HttpResponseRedirect('index.html')
	else:
		form = add_user_form()
		
	return render_to_response('add_user.html', {'form': form,}, RequestContext(request))

### FORM ###
#adds a new user#
class add_user_form(forms.Form):
	username = forms.CharField(max_length=20, label='username')
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20, label='password')

### ACTION ###
#adds a new thread#
def add_thread(request):
	form = add_thread_form(auto_id=False)
	
	if request.method == 'POST':
		form = add_thread_form(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			message = form.cleaned_data['message']
			cursor.execute('INSERT INTO thread VALUES (' + title + ', ' + message + ')')
			return HttpResponseRedirect('index.html')
	else:
		form = add_thread_form()

	return render_to_response('add_thread.html', {'form': form,}, RequestContext(request))
	
### FORM ###
#adds a new thread#
class add_thread_form(forms.Form):
	title = forms.CharField(max_length=100, label='title')
	message = forms.CharField(max_length=1000, label='message')

class login_form(forms.Form):
	username = forms.CharField(max_length=20, label='hello')
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20)

class reply_form(forms.Form):
	reply = forms.CharField(max_length=1000)

