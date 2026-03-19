from django.db import models

class Post(models.Model):
    title =models.CharField(max_length=200)
    content= models.TextField()
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Title