from django.shortcuts import HttpResponse, render


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})


def blog_view(request, *args, **kwargs):
    return render(request, 'blog.html', {})
