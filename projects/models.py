from django.db import models


class Projects(models.Model):
    image = models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length=200)
