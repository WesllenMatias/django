from django.contrib import admin
from .models import Categoria
from .models import Fabricante
from .models import Loja
from .models import Entrada
from .models import Saida
from .models import controleti

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Fabricante)
admin.site.register(Loja)
admin.site.register(Entrada)
admin.site.register(Saida)
admin.site.register(controleti)