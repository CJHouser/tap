from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title       = models.CharField(max_length=256)
    created_at  = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=False)
    content     = models.TextField()
    
    def save(self, *args, **kwargs):
        timestamp = timezone.now()
        if self._state.adding:
            self.created_at = timestamp
        self.modified_at = timestamp
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
