# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TextForm
from sample import core
from forms import TextForm,SearchForm

# Create your views here.
def index(request):
    return render(request, 'textForm.html', {'form': TextForm, 'form2':SearchForm})
def result(request):
    form = SearchForm(request.GET)
    if(form.is_valid()):

        text_content = core.Read(form.data['id'],core.cliente)
        if(text_content):
            return render(request,'Result.html',{'values':text_content})
    return HttpResponseRedirect('/')

def action(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if(form.is_valid()):
            titulo, fecha, cuerpo = core.Scrapper(form.data['url'])
            if(titulo and fecha and cuerpo):
                return HttpResponseRedirect('/result/'+'?id='+str(core.CreateFecha(core.analIce(cuerpo+titulo),fecha,core.cliente)))
    return HttpResponseRedirect('/')
