from django.db import models
from django.utils import timezone
import markdown


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    text_markdown = models.TextField(default='')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def save(self):
        self.text = markdown.markdown(self.text_markdown)
        super(Post, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def __str__(self):
        return self.title
