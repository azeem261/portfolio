from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    post = models.TextField()
