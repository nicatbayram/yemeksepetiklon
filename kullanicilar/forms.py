from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import *

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Kullanıcı Adı',
            'email': 'E-posta',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['password1'].label = 'Şifre'
        self.fields['password2'].label = 'Şifre Tekrar'

        self.fields['username'].widget = widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanici Adi'})
        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifrenizi giriniz'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifrenizi tekrar giriniz'})
        
class UserLoginForm(forms.Form):
   email = forms.EmailField(
       label = 'E-posta',
       widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Giriniz'}))

   password = forms.CharField(
       label = 'Şifre',
       widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifre Giriniz'}))


   def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            self.add_error('email', 'Bu email mevcut değil!')

        return email
   

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('image', 'name',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image'].widget = widgets.FileInput(attrs={'class': 'form-control'})
        self.fields['name'].widget = widgets.TextInput(attrs={'class': 'form-control'})

class UserEditForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']

class ProfilEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['image']

class ChangeUserPassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password Confirmation'})