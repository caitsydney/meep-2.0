from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import login, logout
from meep.views import profile, add_user, add_thread
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', direct_to_template, {'template': 'base.html'}),
	(r'index/$', direct_to_template, {'template': 'index.html'}),
	(r'list/$', direct_to_template, {'template': 'list.html'}),
	(r'reply/$', direct_to_template, {'template': 'reply.html'}),
	(r'style/$', direct_to_template, {'template': 'style.html'}),
	(r'style2/$', direct_to_template, {'template': 'style2.html'}),
	(r'delete_message/$', direct_to_template, {'template': 'delete_message.html'}),
	(r'delete_all_messages/$', direct_to_template, {'template': 'delete_all_messages.html'}),
	#(r'login/', 'meep.views.login'),
	(r'profile/$', profile),
	(r'login/$', login),
	(r'add_thread/$', 'meep.views.add_thread'),
	(r'add_user/$', 'meep.views.add_user')
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
