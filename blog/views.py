from django.shortcuts import get_object_or_404, render

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('-creation_date')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/index.html', context)

def detail(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    return render(request, 'blog/detail.html', {'blog_post': blog_post})
