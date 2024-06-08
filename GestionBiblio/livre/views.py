from django.shortcuts import render,redirect
from django.contrib import admin
from django.http import HttpResponse
from .models import Livres

def index(request):
    return render(request,'livre/index.html')



def Livres_tab(request):
    livres = Livres.objects.all()
    print(livres)
    return render(request, 'livre/index.html', context={"current_tab": "livres","livres":livres})



def save_livres(request):
    Livres_item = Livres(identifiant=request.POST['identifiant'],
                         titre=request.POST['titre'])
    Livres_item.save()
    return redirect('/livres')

def supprimer_livre(request):
    identifiant = request.POST['identifiant']
    Livres.objects.filter(identifiant=identifiant).delete()
    return redirect('/livres')

def supprimer_livres(request):
    identifiant = request.POST.get('identifiant')
    livres = Livres.objects.filter(identifiant=identifiant)
    livres.delete()
    return redirect('/livres')


def modifier_livre(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        nouveau_titre = request.POST.get('nouveau_titre')

        # Vérifier si les données nécessaires sont présentes
        if identifiant and nouveau_titre:
            # Récupérer le livre à modifier
            livre = Livres.objects.get(identifiant=identifiant)
            # Modifier le titre
            livre.titre = nouveau_titre
            # Sauvegarder les modifications
            livre.save()

    return redirect('livre:Livres_tab')

# Create your views here.
