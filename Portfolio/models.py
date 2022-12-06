from distutils.command.upload import upload
from email.mime import image
from tkinter import image_names
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.forms import ImageField, URLField
# Create your models here.

class Proyect(models.Model):
    title = models.CharField (max_length=100,)
    description = models.CharField (max_length=200)
    image = models.ImageField(upload_to="Portfolio/images/")
    url = models.URLField(max_length=200, null=True, blank=True)

    def proyecto(self):
        return "{}{}".format(self.title, self.description)

    def __str__(self):
        return self.proyecto()