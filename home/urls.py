from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'testbook.home.views.home', name='home'),
    url(r'^home/$', 'testbook.home.views.home', name='home'),

)