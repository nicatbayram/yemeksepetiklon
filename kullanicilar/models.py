from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profil(models.Model):
    first_name = models.CharField(max_length= 30, default='empty')
    last_name = models.CharField(max_length= 30, default='empty')
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.isim
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)