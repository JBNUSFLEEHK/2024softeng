from lib2to3.fixes.fix_input import context

from django.shortcuts import render
import pandas as pd


# Create your views here.
def landing(request):
    return render(request,'single_pages/index.html', {'title':'Home'})

def about_me(request):
    return render(request,'single_pages/about_me.html', {'title': 'About Me'})


def naverblog(request):
    return render(request,'single_pages/naver_blog.html', {'title': 'Naver Blog'})

def army_life(request):
    return render(request, 'single_pages/armylife.html', {'title': 'Army life'})



def blog(request):
    df = pd.read_csv('./data.csv')
    post_list = []
    for i, row in df.iterrows():
         post_list.append({
            "title": row["title"],
             "content": row["content"],

         })
    print(post_list)

    return render(request, 'single_pages/blog.html', {'title': 'Blog', 'posts': post_list})






