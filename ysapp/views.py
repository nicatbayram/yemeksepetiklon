from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import *
# from .forms import *
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
            context['restoranlar'] = context['restoranlar'].filter(baslik__icontains = search_input)
            context['search_input'] = search_input
        return context

 

class RestoranDetailView(DetailView):
    model = Restoran
    template_name = 'ysapp/restoran_detay.html'
    context_object_name = 'restorandetay'
