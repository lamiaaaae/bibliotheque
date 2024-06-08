from django.urls import path
from . import views

app_name = 'interface2'
urlpatterns = [
    path('', views.index,name="index"),
    path('abonnes/', views.Abonnes_tab, name="Abonnes_tab"),
    path('save_abonne/', views.save_abonne, name="save_abonne"),
    path('supprimer_abonne/', views.supprimer_abonne, name='supprimer_abonne'),
    path('modifier_abonne/', views.modifier_abonne, name='modifier_abonne'),
]