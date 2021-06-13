from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import EngagementsForms
  
# def index(request):

def form_view(request):
    context = {}
    context['form'] = EngagementsForms()
    return render( request, "index.html", context)

def entity(request):
    return render(request, 'ent.html') 

def engagement(request):
    return render(request, "engage.html")
