from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    summary = models.TextField(max_length=255)

