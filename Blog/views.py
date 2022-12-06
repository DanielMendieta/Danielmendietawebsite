from django.shortcuts import get_object_or_404, render
from .models import Post

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'articulo':posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request, 'post_detail.html', {"post": post})    

# Create your views here.
