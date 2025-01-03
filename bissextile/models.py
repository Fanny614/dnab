from django.db import models

class Bissextile(models.Model):
    endpoint_utilise = models.CharField(max_length=100)
    # Pour le premier endpoint
    annee = models.IntegerField(null=True, blank=True)
    # Pour le deuxième endpoint
    annee_debut = models.IntegerField(null=True, blank=True)
    annee_fin = models.IntegerField(null=True, blank=True)
    # /!\ a exppliquer /!\ Pour le deuxième endpoint on rentre une range d'année
    is_bissextile = models.BooleanField(null=True, blank=True)
    # Sauvegarde de la sortie du deuxième endpoint
    annees_bissextiles = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
