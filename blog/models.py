from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()

    title = models.CharField(max_length=250)
    post = models.TextField()
    def __str__(self):
        return self.title
    def summary(self):
        return self.post[:150]
    def date(self):
        return self.pub_date.strftime('%b %e %Y')
    # GROUPS = (
    #     ('Sports', 'Sports'),
    #     ('Exclusive', 'Exclusive'),
    #     ('Entertainment', 'Entertainment'),
    #     )
    # category = models.CharField(max_length=20,choices=GROUPS, unique=True)
