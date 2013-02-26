from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'testbook.contact.views.contact', name='contact'),
)