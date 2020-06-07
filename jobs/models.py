from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    title = models.CharField(max_length=100, default='title')
    summary = models.TextField(max_length=255)

    def __str__(self):
        return self.title

