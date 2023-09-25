from django.contrib import admin
from reserva.models import Reserva, Petshop

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data', 'turno']
    search_fields = ['nome', 'email', 'nome_pet']
    list_display = ['data', 'turno', 'tamanho']


admin.site.register([Petshop])
