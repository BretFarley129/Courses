# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *
from django.contrib import messages

def index(request):
    context = {}
    context['stuff'] = Course.objects.all()
    
    return render(request,'c/index.html',context)
    


def new(request):
    print request.POST
    name = request.POST['name']
    desc = request.POST['desc']
    x = {'name': name,'desc': desc}
    errors = Course.objects.validate(x)
    if errors:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        
        course = Course.objects.create(name = name, description = desc)
        print Course.objects.all()
    
    return redirect('/')

def delete(request, number):
    x = Course.objects.get(id=number)
    x.delete()
    
    
    return redirect('/')

def destroy(request,number):
    context = {}
    context['stuff'] = Course.objects.get(id = number)
    
    return render(request,'c/destroy.html', context)

