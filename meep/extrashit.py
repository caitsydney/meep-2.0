
	#return render_to_response("add_user.html", {'form' : form,})

### ACTION ###
#adds a new user#
# def add_user(request):
# 	print "enter add_user"
# 	form = add_user_form(auto_id=True)
# 
# 	if request.method == 'POST':
# 		form = add_user_form(request.POST) 
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']
# 			user = auth.authenticate(username=username,password=password)
# 			if user is not None:
# 				print "it worked"
# 			else:
# 				print "nope"


### FORM ###
#adds a new user#
# class add_user_form(forms.Form):
# 	print "enter add_user_form"
# 	username = forms.CharField(max_length=20, label='username')
# 	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20, label='password')


	##sheikgeek	
# def add_user(request):
# 	print "enter add_user"
# 	form = add_user_form(auto_id=True)
# 
# 	if request.method == 'POST':
# 		form = add_user_form(request.POST) 
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']
# 		try:
# 			User.objects.get(username=username)
# 			context = {}
# 			context['error'] = "username already exists"
# 			context.update(csrf(request))
# 			return render_to_response('add_user.html', {'form': form,}, RequestContext(request))				
# #			return render_to_response("add_user.html", context)
# 		except User.DoesNotExist:
# 			User.objects.create_user(username=username, password=password)
# 			if user is not None:
# 				if user.is_active:
# 					auth_login(request, user)
# 					return redirect('/')
# 				else:
# 					return HttpResponse(status=500)
# 			else:
# 					return HttpResponse(status=500)
# 	else:
# 		form = add_user_form()
# 		return render_to_response('add_user.html', {'form': form,}, RequestContext(request))	


# def add_user(request):
# 	print "enter add_user"
# 	conn = sqlite3.connect('meep.db')
# 	cursor = conn.cursor()
# 
# 	#initialize variables to send to template
# 	form = add_user_form(auto_id=True)
# 	
# 	if request.method == 'POST': #if the form is submitted
# 		form = add_user_form(request.POST) 
# 		if form.is_valid(): #if validation rules pass
# 			username = form.cleaned_data['username']
# 			password = form.cleaned_data['password']
# 			cmd = """INSERT INTO meep_user (username,password) VALUES(\'""" + username + """\', \'""" + password + """\');"""
# 			print cmd
# 			cursor.execute(cmd)
# 			conn.commit()
# 			conn.close()
# 			return HttpResponseRedirect('/index/')
# 	else:
# 		form = add_user_form()
# 		
# 	return render_to_response('add_user.html', {'form': form,}, RequestContext(request))

# class login_form(forms.Form):
# 	print "enter login_form"
# 	username = forms.CharField(max_length=20, label='hello')
# 	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=20)

# def login(request):
# 	print "enter login"
# 
# 	username = request.POST["username"]
# 	password = request.POST["password"]
# 	
# 	user = auth.authenticat(username=username, password=password)
# 
# 	if user is not None and user.is_active:
# 		auth.login(request, user)
# 		return HttpResponse("meep/index/")
# 	else:
# 		return HttpResponseRedirect("/invalid_login/")
# 		
# def logout(request):
# 	try:
# 		del request.session['user_id']
# 	except KeyError:
# 		pass
# 	return HttpResponse("You're logged out.")



#############
{% extends "base2.html" %}

{% block title %}create user{% endblock title %}

{% block body %}

	<div class='login_cols'>
		<h3>create an account:</h3>
	
		<div class='indent'>
			<form action='/add_user/' method='POST'> {% csrf_token %}
				{{ form.as_p }}
				<input type="submit" value="submit">
			</form>
		</div>
	</div>
	
{% endblock body %}


