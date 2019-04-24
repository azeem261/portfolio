from django.shortcuts import render, get_object_or_404
from .models import Blog
def blog(request):
    return render(request, 'projects/blogs.html')
def blogpost(request, blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'projects/blogpost.html', {'blog':blogdetail})
