from django.db import models

class Abonnes(models.Model):

    identifiant = models.CharField(max_length=100)
    nom_et_prenom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_et_prenom



# Create your models here.


# Create your models here.
