from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=256)
    creation_date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title
