from django.shortcuts import render, redirect
from .forms import EngagementsForms, RegisterForm
from .models import Engagement, Entity

def form_view(request):
    context = {}
    context['form'] = EngagementsForms()
    return render(request, "index.html", context)

def entity(request):
    return render(request, 'entities.html')

def engagement(request):
    context = {}
    context['engagements'] = Engagement.objects.all()
    return render(request, 'engagements.html', context)

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