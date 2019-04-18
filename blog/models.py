from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    post = models.TextField()
    # GROUPS = (
    #     ('Sports', 'Sports'),
    #     ('Exclusive', 'Exclusive'),
    #     ('Entertainment', 'Entertainment'),
    #     )
    # category = models.CharField(max_length=20,choices=GROUPS, unique=True)
