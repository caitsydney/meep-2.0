from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from meep.models import Message, User, Thread
from django import forms
import sqlite3
import datetime
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

###working functions##
def add_user(request):
	print "enter add_user"
	form = UserCreationForm(request.POST)
	
	if form.is_valid():
		new_user = form.save()
		print "form is valid"
		return HttpResponseRedirect("meep/login/")
	else:
		print "form is not valid"
		form = UserCreationForm()
	
	return render_to_response('add_user.html', {'form': form,}, RequestContext(request))

### ACTION ###
#displays index page#
def index(request):
	print "enter index"
	if request.method == "GET":
		context = {}
		context.update(csrf(request))
		if request.user.is_authenticated():
			#for authenticated users
			print "user is authenticated"
			user_id = request.session['_auth_user_id']
			if user_id:
				user = User.objects.get(id=user_id)
				username = user.username
				context['username'] = username
		return render_to_response('index.html',context)
	else:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth_login(request, user)
				return redirect('/')
		else:
			context = {}
			context['error'] = "invalid login"
			context.update(csrf(request))
			return render_to_response('index.html', context)

### ACTION ###
#login#
def login(request):
	print "enter login"
	username = request.POST['username']
	print username
	password = request.POST['password']
	print password
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/index/")
	else:
		# Show an error page
		return HttpResponseRedirect("/login/")	

def profile(request):
	print "enter profile"
	print "go to index"
	return HttpResponseRedirect("/index/")

def add_thread(request):
	print "enter add_thread"
	conn = sqlite3.connect('meep.db')
	cursor = conn.cursor()

	form = add_thread_form(auto_id=True)

	if request.method == 'POST': #if the form is submitted
		form = add_thread_form(request.POST) 
		if form.is_valid(): #if validation rules pass
			title = form.cleaned_data['title']
			message = form.cleaned_data['message']
			topic = form.cleaned_data['topic']
			date = datetime.now()
			print date
			author = HttpResponse(request.COOKIES["username"])
			print author
			cmd = """INSERT INTO meep_user (username,password) VALUES(\'""" + title + """\', \'""" + message + """\');"""
			cursor.execute('INSERT INTO thread VALUES (' + title + ', ' + message + ')')
			conn.commit()
			conn.close()
			return HttpResponseRedirect('/index/')
	else:
		form = add_user_form()
		
	return render_to_response('add_user.html', {'form': form,}, RequestContext(request))

# FORM ###
#adds a new thread#
class add_thread_form(forms.Form):
	print "enter add_thread_form"
	title = forms.CharField(max_length=100, label='title')
	message = forms.CharField(max_length=1000, label='message')


def logout(request):
	auth_logout(request)
	return redirect('/')

class reply_form(forms.Form):
	print "enter reply_form"
	reply = forms.CharField(max_length=1000)


