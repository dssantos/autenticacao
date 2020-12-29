from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'categoria']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria']
