from .models import *
from django import forms

class YemekForm(forms.ModelForm):
    
    class Meta:
        model = Yemek
        fields = ["yemekadi","resim"]

        widgets = {
            'yemekadi': forms.Textarea(attrs={'class':'form-control'}),
        }
