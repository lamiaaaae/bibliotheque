from django.contrib import admin
from .models import Abonnes

class AbonnesAdmin(admin.ModelAdmin):
    list_display = ('identifiant','nom_et_prenom')
    search_fields = ['nom_et_prenom']


admin.site.register(Abonnes,AbonnesAdmin)


# Register your models here.

# Register your models here.
