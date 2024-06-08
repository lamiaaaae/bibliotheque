from django.contrib import admin
from .models import Livres

class LivresAdmin(admin.ModelAdmin):
    list_display = ('identifiant','titre')
    search_fields = ['titre']


admin.site.register(Livres,LivresAdmin)


# Register your models here.
