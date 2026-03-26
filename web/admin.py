from django.contrib import admin
from .models import Cliente
from .models import Perfil

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Esto define las columnas que verás en la tabla
    list_display = ('nombre', 'correo', 'edad', 'activo')
    # Esto agrega un buscador por nombre
    search_fields = ('nombre',)
    # Esto agrega un filtro lateral por estado activo
    list_filter = ('activo',)
    ordering = ('nombre',)

admin.site.register(Perfil)