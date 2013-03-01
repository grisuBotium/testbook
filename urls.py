from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # This is going to be our home view.
    # We'll uncomment it later
    url(r'^$', include('testbook.home.urls')),
    url(r'^home/$', include('testbook.home.urls')),
    url(r'^login/$', 'testbook.login.views.login_view', name='login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/$', include('testbook.about.urls')),
    url(r'^contact/$', include('testbook.contact.urls')),

    # login required
    url(r'^stream/$', include('testbook.stream.urls')),
    url(r'^project/$', include('testbook.project.urls'))

)

# Uncomment these two lines to enable your static files on PythonAnywhere
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()