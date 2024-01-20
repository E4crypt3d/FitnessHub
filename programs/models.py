from django.db import models
from PIL import Image

# Create your models here.


class Exercise(models.Model):
    title = models.CharField(max_length=90)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='excercise', max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Open the image file
        img = Image.open(self.image.path)

        # Resize the image (adjust these values as needed)
        new_width = 400
        new_height = 300
        resized_img = img.resize((new_width, new_height))

        # Save the resized image back to the same path
        resized_img.save(self.image.path)
