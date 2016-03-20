from django.db import models

class Post(models.Model):

    title = models.CharField(max_length = 30)
    content = models.TextField()
    create_at = models.DateTimeField(
            auto_now_add = True, 
            )
    update_at = models.DateTimeField(
            auto_now = True,
            )

    class META:
        verbose_name = "POST"
        verbose_name_plura= verbose_name


    def __str__(self,):
        return self.title





