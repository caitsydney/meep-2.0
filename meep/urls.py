from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', direct_to_template, {'template': 'base.html'}),
	(r'login/$', direct_to_template, {'template': 'login.html'}),
	(r'logout/$', direct_to_template, {'template': 'logout.html'}),
	(r'login/$', direct_to_template, {'template': 'login.html'}),
	(r'list/$', direct_to_template, {'template': 'list.html'}),
	(r'reply/$', direct_to_template, {'template': 'reply.html'}),
	(r'style/$', direct_to_template, {'template': 'style.html'}),
	(r'style2/$', direct_to_template, {'template': 'style2.html'}),
	(r'login/$', direct_to_template, {'template': 'login.html'}),
	(r'delete_message/$', direct_to_template, {'template': 'delete_message.html'}),
	(r'delete_all_messages/$', direct_to_template, {'template': 'delete_all_messages.html'}),
	#(r'add_thread/$', direct_to_template, {'template': 'add_thread.html'}),
	(r'add_thread/$', 'meep.views.add_thread'),
	(r'add_user/$', 'meep.views.add_user')
	
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
