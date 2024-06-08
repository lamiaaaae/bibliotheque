from django.db import models

class Livres(models.Model):

    identifiant = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre



# Create your models here.
