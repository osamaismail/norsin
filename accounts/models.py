from django.db import models
from PIL import Image
from django.contrib.auth.models import User






class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_pic = models.ImageField(upload_to="user_pic")

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Blogger, self).save(*args, **kwargs)
        user_pic = Image.open(self.user_pic.path)
        if user_pic.height > 300 or user_pic.width > 300:
            output_size = (300,300)
            user_pic.thumbnail(output_size)
            user_pic.save(self.user_pic.path)
