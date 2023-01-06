from django.db import models

# Create your models here.
class Image(models.Model):
    image_before = models.FileField(upload_to='images/before')
    image_after = models.FileField(upload_to='images/after')
