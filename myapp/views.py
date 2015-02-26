from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Post, Comment
from datetime import datetime

def index(request):
    posts = Post.objects.order_by('-date')
    context = {'latest_posts': posts}
    return render(request, 'myapp/index.html', context)
    
def post(request, post_id):
    p = Post.objects.get(id=post_id)
    return render(request, 'myapp/post.html', {'post': p,
                                               'comments': p.comment_set.all()})
    
def add_post(request):
    p = Post(header = request.POST['header'], text = request.POST['text'])
    p.save()
    return redirect('index')
    
def add_comment(request):
    post_id = request.POST['post']
    post = Post.objects.get(id = post_id)
    c = Comment(text = request.POST['text'])
    post.comment_set.add(c)
    return redirect('post', post_id)
    
def admin(request):
    return HttpResponse("ишь чё захотел, нету тут админки :)")