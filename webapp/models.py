from django.db import models
# from djoser import urls
# Create your models here.
    
class Blog(models.Model):
    image=models.FileField(upload_to="uploads/blogs/")
    title=models.CharField(max_length=255)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}:{self.body}"