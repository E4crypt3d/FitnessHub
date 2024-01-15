from django.db import models

# Create your models here.


class Exercise(models.Model):
    title = models.CharField(max_length=90)
    body = models.TextField(max_length=280)
    image = models.ImageField(upload_to='excercise', max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
