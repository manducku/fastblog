from django.db import models 
from posts.models import Post 


class Comment(models.Model):
    
    post = models.ForeignKey(Post)
    content = models.CharField(max_length=20)
    create_at = models.DateTimeField(
        auto_now_add=True,
        )
    update_at=models.DateTimeField(
            auto_now=True, 
            )

    class META:
        verbose_name="comment"
        verbose_name_plusa=verbose_name

    def __str__(self):
        return post.id


