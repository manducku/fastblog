from posts.models import Post 
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

def post_detail(request, pk):

    post = Post.objects.get(pk=pk)
    
    context = {
            "post": post,
            }

    return render(
            request, 
            "posts/post.html",
            context = context,
            )


