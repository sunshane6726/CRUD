from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self): # 가장먼저 title 나와라 라고 하기위해서 있다.
        return self.title
