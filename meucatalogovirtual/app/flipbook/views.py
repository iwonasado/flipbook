# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from models import FlipBook, FlipBookPage
from django.template.defaultfilters import slugify
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from pdftojpg import pdftojpg
from descompactador import Descompactador
from django.contrib import messages
from django.conf import settings
from django.template import RequestContext
from django.db import IntegrityError
import os

def inicial(request,slug):
	flipbook  = get_object_or_404(FlipBook, slug = slug)
	return render_to_response('flipbook/inicial.html', {
        'flipbook': flipbook,
    }, context_instance=RequestContext(request))

def flipbook(request,slug):
	flipbook  = get_object_or_404(FlipBook, slug = slug)
	pages = FlipBookPage.objects.filter(gallery = flipbook).order_by('numero')
	return render_to_response('flipbook/flipbook.html', {
        'flipbook': flipbook,
        'pages':pages,
    }, context_instance=RequestContext(request))

def create(request):
	if request.method == 'POST':
		if request.POST['redirect']:
			redirect = request.POST['redirect']
		else:
			redirect = '/'
		if request.user.is_authenticated():
			subtitulo = texto = logo = capa = None
			if request.POST['titulo']:
				titulo = request.POST['titulo']
				if request.POST['subTitulo']:
					subtitulo = request.POST['subTitulo']
				if request.POST['texto']:
					texto = request.POST['texto']
				if request.FILES.has_key('logo'):
					logo = request.FILES['logo']
				if request.FILES.has_key('capa'):
					capa = request.FILES['capa']
				try:
					flipbook = FlipBook.objects.create(usuario = request.user,titulo=titulo,slug = slugify(titulo), subTitulo = subtitulo, texto=texto,image = capa, logo=logo)
				except IntegrityError:
					messages.error(request, (u'Título ja existe!'))
					return HttpResponseRedirect('/home/')
				if request.FILES.has_key('paginas'):
					paginas = request.FILES['paginas']
					file_ = default_storage.save(paginas.name, ContentFile(paginas.read()))
					ext = os.path.splitext(file_)[1]
					if ext == '.pdf':
						pdf = pdftojpg(settings.PROJECT_ROOT+'/media/'+file_,settings.PROJECT_ROOT+'/media/flipbook/'+str(request.user)+'/'+slugify(titulo)+'/img')
						content = pdf.content
					elif ext =='.zip':
						zip = Descompactador()
						zip.zip(settings.PROJECT_ROOT+'/media/'+file_,settings.PROJECT_ROOT+'/media/flipbook/'+str(request.user)+'/'+slugify(titulo)+'/img')
						content = zip.content
					else:
						content = None
					for index,item in enumerate(content):
						FlipBookPage.objects.create(gallery = flipbook,image='/media/flipbook/'+str(request.user)+'/'+slugify(titulo)+'/img/'+item,numero = index)
				return HttpResponseRedirect(redirect)
			return HttpResponseRedirect(redirect)
		messages.error(request, (u'Usuário deve estar logado!'))
		return HttpResponseRedirect(redirect)
	else:
		return HttpResponseRedirect('/')
