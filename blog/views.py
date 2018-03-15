from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, EditPostForm
from django.utils import timezone

# Create your views here.
def get_blog_page(request):
    posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()
                               ).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})
    
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blog/post_detail.html", {'post': post})

#//////////////////////////////

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        
        return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

#//////////////////////////////

def edit_blog_detail(request, id): 
    post = get_object_or_404(Post, pk=id)

    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.pk)
    else:
        form = EditPostForm(instance=post)
    
    return render(request, "blog/create_post.html", {'form': form})

  
