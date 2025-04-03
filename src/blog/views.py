from django.shortcuts import render

def blog_views(request):
    return render(request, 'blog.html', {})
