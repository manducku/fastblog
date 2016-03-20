from django.shortcuts import render,redirect
from posts.models import Post 
from django.core.urlresolvers import reverse
from django.views.generic import View, ListView, CreateView 
from .post_base import PostBaseView

class PostListView(PostBaseView, CreateView):
    template_name="posts/post_list.html"
    fields= [
            "title",
            "content",
           ] 
    
    def get_context_data(self, **kwargs):
        kwargs['posts']=Post.objects.all()
        return super(PostListView, self).get_context_data(**kwargs)
   
    def get_success_url(self,**kwargs):
        return reverse("post-list")



