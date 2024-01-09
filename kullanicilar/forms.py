from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='İsim',max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim'}))

    last_name = forms.CharField(label='Soyisim',max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'email': 'E-posta',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['password1'].label = 'Şifre'
        self.fields['password2'].label = 'Şifre Tekrar'

        self.fields['email'].widget = widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta'})
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Şifrenizi giriniz'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Şifrenizi tekrar giriniz'})

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.username = user.email  
        if commit:
            user.save()
        return user
        
class UserLoginForm(forms.Form):
   email = forms.EmailField(
       label = 'E-posta',
       widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Giriniz'}))

   password = forms.CharField(
       label = 'Şifre',
       widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Şifre Giriniz'}))


   def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email = email).exists():
            self.add_error('email', 'Bu email mevcut değil!')

        return email
