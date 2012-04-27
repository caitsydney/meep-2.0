from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context
from meep.models import Message, User, Thread
from django import forms
import sqlite3
import datetime
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def home(request):
	print "enter home"
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/registration/login/")
	else:
		return HttpResponseRedirect("/index/")

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
	
	return render_to_response('registration/add_user.html', {'form': form,}, RequestContext(request))

def index(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/registration/login/")	
	if request.method == "GET":
		context = {}
		context.update(csrf(request))
		if request.user.is_authenticated():
			#for authenticated users
			print "user is authenticated"
			user_id = request.session['_auth_user_id']
			if user_id:
				user = User.objects.get(id=user_id)
				context['user'] = user
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

def login(request):
	print "enter login"
	if request.method == "POST":
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
	else:
		form = login_form()	
	return render_to_response('accounts/login.html', {'form': form,}, RequestContext(request))
	

def profile(request):
	print "enter profile"
	print "go to index"
	return HttpResponseRedirect("/index/")

def add_thread(request):
	check_auth(request)
	print "enter add_thread"
	form = add_thread_form(auto_id=True)
	if request.method == 'POST': #if the form is submitted
		title = request.POST['title']
		body = request.POST['message']
		
		user_id = request.session['_auth_user_id']
		if user_id:
			user = User.objects.get(id=user_id)
		creator = user
		
		created = datetime.datetime.now()
		thread = Thread(title=title, creator=creator, created=created)
		thread.save()
		message = Message(title=title, body=body, creator=creator, created=created, thread=thread)
		message.save()
		return HttpResponseRedirect('/list_threads/')
	return render_to_response('add_thread.html', {'form': form,}, RequestContext(request))


def list_threads(request):
	check_auth(request)
	print "enter list_thread"
	threads = Thread.objects.order_by("created")
	c = Context({"threads": threads})
	return render_to_response('list_threads.html', c)

def add_message(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/registration/login/")	
	print "enter add_message"
	form = add_message_form(auto_id=True)
	if request.method == 'POST': #if the form is submitted
		title = request.POST['title']
		body = request.POST['message']
		
		user_id = request.session['_auth_user_id']
		if user_id:
			user = User.objects.get(id=user_id)
		creator = user
		
		created = datetime.datetime.now()
		thread = Thread(title="default", creator=creator, created=created)
		thread.save()
		message = Message(title=title, body=body, creator=creator, created=created, thread=thread)
		message.save()
		return HttpResponseRedirect('/list_messages/')
	return render_to_response('add_message.html', {'form': form,}, RequestContext(request))

def list_messages(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/registration/login/")	
	print "enter list messages"
	messages = Message.objects.order_by("created")
	c = Context({"messages": messages})
	return render_to_response('list_messages.html', c)

#def list_messages(request, thread_id):	
#	thread = get_object_or_4040(Thread.objects.select_related(), pk=threadid)
#	posts = thread.posts.all().select_related()
#	c = Context({"posts": posts})
#	return render_to_response(thread.get_absolute_url(), c)

def logout(request):
	auth.logout(request)
	return  HttpResponseRedirect("/registration/login/")

def check_auth(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/registration/login/")	

class add_thread_form(forms.Form):
	print "enter add_thread_form"
	title = forms.CharField(max_length=100, label='title')
	message = forms.CharField(max_length=1000, label='message')
	
class add_message_form(forms.Form):
	print "enter add_message_form"
	title = forms.CharField(max_length=100, label='title')
	message = forms.CharField(max_length=1000, label='message')

class login_form(forms.Form):
	print "enter login_form"
	username = forms.CharField(max_length=20, label='hello')
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20)

class reply_form(forms.Form):
	print "enter reply_form"
	reply = forms.CharField(max_length=1000)


