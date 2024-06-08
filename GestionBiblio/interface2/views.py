from django.shortcuts import render,redirect
from django.contrib import admin
from django.http import HttpResponse
from .models import Abonnes

def index(request):
    return render(request,'interface2/index.html')

'''def Livres(request):
    return render(request, 'index.html',context={"current_tab": "Livres"})'''

def Abonnes_tab(request):
    abonnes = Abonnes.objects.all()
    return render(request, 'interface2/index.html', context={"current_tab": "abonnes","abonnes":abonnes})



def save_abonne(request):
    Abonnes_item = Abonnes(identifiant=request.POST['identifiant'],
                         nom_et_prenom=request.POST['nom_et_prenom'])
    Abonnes_item.save()
    return redirect('/abonnes')

def supprimer_abonne(request):
    identifiant = request.POST['identifiant']
    Abonnes.objects.filter(identifiant=identifiant).delete()
    return redirect('/abonnes')

'''def supprimer_livres(request):
    identifiant = request.POST.get('identifiant')
    livres = Livres.objects.filter(identifiant=identifiant)
    livres.delete()
    return redirect('/livres')'''


def modifier_abonne(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        nouveau_nom_et_prenom = request.POST.get('nouveau_nom_et_prenom')

        # Vérifier si les données nécessaires sont présentes
        if identifiant and nouveau_nom_et_prenom:
            # Récupérer le livre à modifier
            abonne = Abonnes.objects.get(identifiant=identifiant)
            # Modifier le titre
            abonne.nom_et_prenom = nouveau_nom_et_prenom
            # Sauvegarder les modifications
            abonne.save()

    return redirect('interface2:Abonnes_tab')

# Create your views here.
