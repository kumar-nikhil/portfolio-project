from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(blank=True, null=True, default=None)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:50]

    def date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')