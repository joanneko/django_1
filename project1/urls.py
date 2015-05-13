from django.conf.urls import patterns, include, url
from project1.views import display_meta, hello, current_datetime, hours_ahead, hours_behind
from django.contrib import admin
admin.autodiscover() 
from books import views as books_views 
from contact import views as contact_views 


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$', hello),
	('^$', hello),
	('^time/$', current_datetime), 
	(r'^time/plus/(\d{1,2})/$', hours_ahead),
	(r'^time/minus/(\d{1,2})/$', hours_behind),
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^project1/', include('project1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^search/$', books_views.search),
    (r'^contact/$', contact_views.contact)
)
