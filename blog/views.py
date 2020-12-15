from django.shortcuts import get_object_or_404, render

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('-creation_date')
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/index.html', context)

def detail(request, blog_post_id):
    #TODO: clean the next and prev post queries up. it works for now, but
    # there has got to be a cleaner way to accomplish this
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    next_post = BlogPost.objects.filter(creation_date__gt=blog_post.creation_date).order_by('creation_date').first() 
    prev_post = BlogPost.objects.filter(creation_date__lt=blog_post.creation_date).order_by('-creation_date').first()
    if blog_post == next_post:
        next_post = None
    if blog_post == prev_post:
        prev_post = None
    context = {
        'blog_post': blog_post,
        'next_post': next_post,
        'prev_post': prev_post,
    }
    return render(request, 'blog/detail.html', context)
