from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from meep.models import Message, User, Thread
from django import forms

def index(request):
	print "enter index"
	return render_to_response('meep/index.html')

def add_user_action(request):
	if request.method == 'POST':
		form = add_user_form(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			pw = form.cleaned_data['password']
			cursor.execute('INSERT INTO user VALUES (' + username + ', ' + 'pw)')
			return HttpResponseRedirect('index.html')
	else:
		form = add_user_form()
	return render_to_response('create_user.html', {'form': form,})

class add_user_form(forms.Form):
	user = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20)
