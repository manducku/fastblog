from django.shortcuts import render,redirect
from posts.models import Post 

def posts(request):
    
    context = { 
        "posts" = Post.objects.all()
            }

    return render(
            request,
            "posts/posts.html",
            context = context, 
            )


