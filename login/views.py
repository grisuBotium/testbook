__author__ = 'bruno'

from django.shortcuts import render_to_response
from django.template import RequestContext
from testbook.login.forms import LoginForm
from testbook.customuser.models import CustomUser
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def login_view(request):
    def errorHandle(error):
        form = LoginForm()
        return render_to_response('login.html', {
            'error' : error,
            'form' : form,
            }, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponseRedirect('/stream')

                else:
                    error = 'account disabled!'
                    return errorHandle(error)
            else:
                error = 'wrong username/password!'
                return errorHandle(error)
        else:
            error = 'invalid input!'
            return errorHandle(error)
    else:
        form = LoginForm()
        return render_to_response('login.html', {
            'form' : form,
            }, context_instance=RequestContext(request))