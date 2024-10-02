from django.contrib import admin
from .models import Categoria, Opcoes, Adicional, Produto

admin.site.register(Categoria)
admin.site.register(Opcoes)
admin.site.register(Adicional)
admin.site.register(Produto)
