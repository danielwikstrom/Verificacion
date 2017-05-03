# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TextForm
from sample import core
from forms import TextForm

# Create your views here.
def index(request):
    return render(request, 'textForm.html', {'form': TextForm})
def result(request):
    id = request.GET['id']
    text_content = core.ReadString(id,core.cliente)
    print type(text_content)
    return render(request,'Result.html',{'text_content':text_content})
def action(request):

    if request.method == 'POST':
        form = TextForm(request.POST)
        queryResult = core.analIce(form.data['text_content'])
        id = core.Create(queryResult,core.cliente)
        if(form.is_valid()):
            return HttpResponseRedirect('/result/'+'?id='+str(id))

