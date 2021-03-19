from django.contrib import admin
from .models import Contato, Categoria


class ContatoAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'sobrenome',
        'telefone',
        'categoria',
        'ativo'
    )
    list_display_links = (
        'nome',
        'sobrenome'
    )
    list_editable = (
        'telefone',
        'ativo'
    )
    list_filter = ('categoria', )
    search_fields = (
        'nome', 
        'sobrenome', 
        'telefone'
    )
    list_per_page = 10


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
