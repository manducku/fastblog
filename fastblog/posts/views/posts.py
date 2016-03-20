from django.shortcuts import render,redirect
from posts.models import Post 
from django.core.urlresolvers import reverse

def posts(request):

    if(request.method =="GET"):
        context = { 
                "posts": Post.objects.all()
                }
        print ("hello")
        return render(
                request,
                "posts/posts.html",
                context = context, 
                )
        
    if(request.method =="POST"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        post=Post.objects.create(
                title=title,
                content=content,
                )
        return redirect(
                reverse(
                    "posts"
                    )
                )


