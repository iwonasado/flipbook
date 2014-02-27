# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import forms, authenticate, views, login
from django import http
from django.core.urlresolvers import reverse
from models import UserProfile
from forms import FormRegistro
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def mylogin(request):
    redirect_to = request.REQUEST.get('next', '/')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(redirect_to or request.META.get('HTTP_REFERER', None))
        else:          
            messages.error(request, ('Nome de usuario ou senha errados.'))  
    return render_to_response('account/login.html', {
    	'redirect_to': redirect_to,
    }, context_instance=RequestContext(request))
         
 
@login_required()
def logout(request):
    """Destroy user session."""
    auth.logout(request)
    messages.success(request, ('Saiu do sistema com sucesso.'))
    return http.HttpResponseRedirect('/')

def registrar(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            novo_usuario = form.save()
            return HttpResponseRedirect('/')
    else:
        form = FormRegistro()
        
    return render_to_response(
        'account/registrar.html',
        {'form':form},
        context_instance=RequestContext(request),
        )

def avaiableUser(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).count():
            print 'ja existe'
            return HttpResponse(content = u'<span style="font-size:150%">'+request.POST['username']+'</span>  em Uso!', mimetype='text/string')
        else:
            print 'Não existe'
            return HttpResponse(content ='0', mimetype='text/string')
    else:
        print 'erro!'
        return HttpResponse(content ='-1', mimetype='text/string')

def avaiableEmail(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).count():
            print 'ja existe'
            return HttpResponse(content = u'<span style="font-size:150%">'+request.POST['email']+'</span> em uso!', mimetype='text/string')
        else:
            print 'Não existe'
            return HttpResponse(content ='0', mimetype='text/string')
    else:
        print 'erro!'
        return HttpResponse(content ='-1', mimetype='text/string')
