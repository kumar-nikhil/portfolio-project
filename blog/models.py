from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(blank=True, null=True, default=None)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image_blog/', blank=True)
