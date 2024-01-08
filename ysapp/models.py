from django.db import models
from django.urls import reverse

# Create your models here.
class Restoran(models.Model):
    restoranadi = models.CharField(max_length=10000)
    puan = models.IntegerField()


    def __str__(self):
        return self.restoranadi
    
    def get_absolute_url(self):
        return reverse("ysapp:restorandetay", kwargs={"pk": self.pk})
    
    
class Yemek(models.Model):
    restoran = models.ForeignKey(Restoran, related_name="restoran", on_delete=models.DO_NOTHING)
    yemekadi = models.CharField(max_length=100)
    
    def __str__(self):
        return self.yemekadi
    
    def get_absolute_url(self):
        return reverse("ysapp:restorandetay", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)