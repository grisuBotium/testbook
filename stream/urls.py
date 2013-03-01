from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'testbook.stream.views.stream', name='stream'),

)