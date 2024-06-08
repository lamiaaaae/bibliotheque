from django.urls import path
from . import views

app_name = 'livre'
urlpatterns = [
    path('', views.index,name="index"),
    path('livres/', views.Livres_tab, name="Livres_tab"),
    path('save_livres/', views.save_livres, name="save_livres"),
    path('supprimer_livre/', views.supprimer_livre, name='supprimer_livre'),
    path('modifier_livre/', views.modifier_livre, name='modifier_livre'),
]
