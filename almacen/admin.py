from django.contrib import admin
from .models import SeccionProd, Articulos

# Register your models here.

class SeccionProdAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ArticulosAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(SeccionProd, SeccionProdAdmin)

admin.site.register(Articulos, ArticulosAdmin)
