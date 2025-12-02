from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_id = models.IntegerField()  # store User Service user ID
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
