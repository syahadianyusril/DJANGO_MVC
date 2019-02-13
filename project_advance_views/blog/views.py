from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm
from django.utils import timezone

# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blogs':blog})
# 
def form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('blog')
# 
    else:
        form = PostForm()
    return render(request,'blog/form_blog.html', {'form': form})