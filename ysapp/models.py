from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Restoran(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    restoranadi = models.CharField(max_length=10000)
    resim =  models.ImageField(upload_to='restoran_images', null= True)


    def __str__(self):
        return self.restoranadi
    
    def get_absolute_url(self):
        return reverse("ysapp:restorandetay", kwargs={"pk": self.pk})
    
    
class Yemek(models.Model):
    restoran = models.ForeignKey(Restoran, related_name="yemek", on_delete=models.DO_NOTHING)
    kullaniciadi = models.CharField(max_length=100, null=True)
    yemekadi = models.TextField(null=True, blank=True)
    resim =  models.ImageField(upload_to='yemek_images', null= True)
    
    def __str__(self):
        return self.yemekadi
    
    def get_absolute_url(self):
        return reverse("ysapp:restorandetay", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)