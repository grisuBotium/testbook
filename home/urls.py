from django.conf.urls import patterns, url, include
from django.views.generic.simple import redirect_to

from home import views

urlpatterns = patterns('',

    url(r'^$', 'testbook.home.views.home', name='home'),

)