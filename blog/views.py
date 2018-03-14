from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

# Create your views here.
def get_blog_page(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/post_detail.html", {'post': post})
    
def create_post(request):
    form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})
  
# def create_blog_post(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()

#     form = PostForm()
#     items = Post.objects.all()
#     return render(request, "blog/blog_post_form.html", {'items': items, 'form': form})
