from django.shortcuts import render, redirect
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import EngagementsForms, RegisterForm

# def index(request):


def form_view(request):
    context = {}
    context['form'] = EngagementsForms()
    return render(request, "index.html", context)


def entity(request):
    return render(request, 'entities.html')


def engagement(request):
    return render(request, "engagements.html")


def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "signup.html", {"form": form})

def home(response):
	return render(response, "index.html", {})