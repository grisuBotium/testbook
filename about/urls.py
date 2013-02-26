from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'testbook.about.views.about', name='about'),

)