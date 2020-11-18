from django.shortcuts import render

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('-creation_date')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'posts/index.html', context)
