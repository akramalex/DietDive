from django.db import models
from cloudinary.models import CloudinaryField

""" Create your models here.

This module defines the `About` model for the `About` page.
It includes fields for the title, profile image,
content, and the date when it was last updated.
"""


class About(models.Model):
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
