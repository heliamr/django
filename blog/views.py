from django.shortcuts import render
from .models import Post
from django.shortcuts import get_list_or_404

# Create your views here.
def index(request):
    return render(request , 'blog/index.html' , {})

def post(request , slug):
    p = get_list_or_404(Post , slug = slug)
    return render(request , 'blog/post.html' , {'post': p})

def posts(request):
    all_posts = Post.objects.all().order_by('-created_at')[:10]
    return render(request , 'blog/posts.html' , {'p': all_posts})
