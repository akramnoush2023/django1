from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExit:
#         raise Http404("No post found")
#     return render(request, 'blog/post/detail.html', {'post': post})

    post = get_object_or_404(
        Post, 
        status=Post.Status.PUBLISHED, 
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, 'blog/post/detail.html', {'post': post})