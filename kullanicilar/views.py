from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from .models import *


# Create your views here.
def kayitol(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            kullaniciadi = form.cleaned_data.get('username')
            messages.success(request, f'Hesabınız başarıyla oluşturuldu: {kullaniciadi} , tekrar giriş yapınız.')
            return redirect('ysapp:anasayfa')
    else:
        form = UserRegisterForm()

    return render(request, 'kullanicilar/kayitol.html', {'form': form})



def girisyap(request):

    if request.user.is_authenticated:
        return redirect('ysapp:anasayfa') 

    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            username = User.objects.get(email = email).username

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('ysapp:anasayfa')

            else:
                return render(request, 'kullanicilar/girisyap.html', {
                    'form': form
                })
        else:
            return render(request, 'kullanicilar/girisyap.html', {
                    'form': form
                })
    else:
        form = UserLoginForm()
        return render(request, 'kullanicilar/girisyap.html', {
            'form': form
        })

@login_required
def cikisyap(request):
    logout(request)
    return redirect('ysapp:anasayfa')