from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib import messages
from .models import Perfil

class PerfilUpdateView(UpdateView):
    model = Perfil
    fields = ['bio']
    template_name = 'clientes/perfil_form.html' # Ruta a la plantilla
    success_url = reverse_lazy('inicio') # Redirigir a una URL de éxito (ej. 'inicio')

    def form_valid(self, form):
        messages.success(self.request, '¡Tu perfil se ha actualizado con éxito!')
        return super().form_valid(form)
