from posts.models import Post
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .post_base import PostBaseView
from django.views.generic import DetailView 
from django.contrib.auth.decorators import login_required

@login_required()
def post_detail(request, pk):
    
    post = Post.objects.get(pk=pk)
    if(request.method =="GET"):
        context = {
                "post": post,
                }

        return render(
                request, 
                "posts/post_detail.html",
                context = context,
                )
    if(request.method=="POST"):
        comment = post.comment_set.create(
                content=request.POST.get("content")
                )

        return redirect(
                reverse(
                    "post-detail", 
                    kwargs={
                        'pk':post.id,
                        },
                    ), 
                )



