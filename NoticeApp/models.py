from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="notice")

    def __str__(self):
        return self.title


class Comment(models.Model): 
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)