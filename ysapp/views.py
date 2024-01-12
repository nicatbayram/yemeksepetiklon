from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

def anasayfa(request):
    return render(request, 'ysapp/anasayfa.html')

class RestoranListView(ListView):
    model = Restoran
    template_name = 'ysapp/restoran_view.html'
    context_object_name = 'restoranlar'
    ordering = ['restoranadi']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['restoranlar'] = context['restoranlar'].filter(restoranadi__icontains = search_input)
            context['search_input'] = search_input
        return context

 

class RestoranDetailView(DetailView):
    model = Restoran
    template_name = 'ysapp/restoran_detay.html'
    context_object_name = 'restorandetay'

class RestoranCreateView(LoginRequiredMixin ,CreateView):
    model = Restoran
    fields = ['restoranadi','resim']
    template_name = 'ysapp/restoran_olustur.html'
    context_object_name = 'restoranolustur'

    def form_valid(self, form):
        form.instance.kullanici = self.request.user
        return super().form_valid(form)
            
    
class YemekAddView(LoginRequiredMixin ,CreateView):
    model = Yemek
    form_class = YemekForm
    template_name = 'ysapp/yemek_add.html'

    def form_valid(self, form):
        restoran_id = self.kwargs.get('pk')  
        restoran = get_object_or_404(Restoran, pk=restoran_id)
        form.instance.restoran = restoran  
        form.instance.kullaniciadi = self.request.user.username  
        return super().form_valid(form)       
    success_url = reverse_lazy('yspp:restoranlar')