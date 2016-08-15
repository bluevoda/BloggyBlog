from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Post, Comment
from django import forms
from .forms import CommentForm

# Create your views here.
def homepage(request):
    posts = Post.objects.filter(isPublished = True)
    return render(request, 'home.html',
                  {
                      'name':'Emre',
                      'posts':posts
                  })

def showpost(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post = id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post_id = id
            form.save()


    return (render(request, 'post_detail.html',{
        'post': post,
        'comments': comments,
        'form' : form
    }))

def about(request):
    return HttpResponse("aboutme")
