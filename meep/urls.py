from django.conf.urls import patterns, include, url
from meep.views import *
#from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('meep.views',
	(r'login/$', 'login'),
	(r'index/$', 'index'),
	(r'^$', 'home'),
	(r'logout/$', 'logout'),
	(r'add_thread/$', 'add_thread'),
	(r'add_user/$', 'add_user'),
	(r'list_threads/$', 'list_threads')
#	(r'^thread/(?P<thread_id>\d+)/$', 'list_messages'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
