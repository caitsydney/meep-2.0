from django.conf.urls import patterns, include, url
from meep.views import *
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('meep.views',
	(r'^$', 'home'),
	(r'index/$', 'index'),
	(r'login/$', 'login'),
	(r'logout/$', 'logout'),
	(r'add_user/$', 'add_user'),
	(r'add_thread/$', 'add_thread'),
	(r'add_message/$', 'add_message'),
	(r'list_threads/$', 'list_threads'),
	(r'list_messages/$', 'list_messages'),
#	(r'^thread/(?P<thread_id>\d+)/$', 'get_thread'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
