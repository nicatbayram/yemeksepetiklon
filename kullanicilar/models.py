from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from PIL import Image

# Create your models here.
class Profil(models.Model):
    name = models.CharField(max_length= 30, default='empty')
    image = models.ImageField(upload_to='profile_pic')
    kullanici = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    slug = AutoSlugField(populate_from = 'name', unique=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)