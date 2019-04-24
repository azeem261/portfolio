from django.http import HttpResponse
from django.shortcuts import render
from .models import Projects
from blog.models import Blog
def home(request):
    projects = Projects.objects
    blog = Blog.objects
    return render(request, 'projects/index.html', {'projects':projects,'blog':blog})
def homepage(request):
    return render(request, 'home.html')
