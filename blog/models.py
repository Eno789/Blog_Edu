from django.conf import settings
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    caption = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(blank=True)
    publish = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def caption_len(self):
        return len(self.caption)

class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(max_length=500)

    class Meta:
        ordering = ['-id']