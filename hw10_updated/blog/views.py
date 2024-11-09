from django.shortcuts import render
from .models import Post

def blog(request):
    posts = Post.objects.all().order_by('-pk')
    return render(request,'blog/blog.html',{'title' : 'Blog', 'posts': posts})

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )
def index(request):
    return render(request,'blog/index.html', {'title':'Home'})

def about_me(request):
    return render(request,'blog/about_me.html', {'title': 'About Me'})


def naverblog(request):
    return render(request,'blog/naver_blog.html', {'title': 'Naver Blog'})

def army_life(request):
    return render(request, 'blog/armylife.html', {'title': 'Army life'})


