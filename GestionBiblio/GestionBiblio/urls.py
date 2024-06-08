from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livres/', include("livre.urls")),
    path('abonnes/', include("interface2.urls")),
    path('', include("accueil.urls")),

]
