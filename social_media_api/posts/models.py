from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Post(models.Model):
    title = models.CharField(blank=False)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.content