from typing import Any

from ninja import NinjaAPI

from bissextile.models import Bissextile
from bissextile.utils import est_bissextile

api = NinjaAPI()


@api.post('/bissextile/single/{annee}')
def single(request, annee: int) -> str:
    """"
    Prend en entrée une année.
    Regarde si elle est bissextile.
    Sauvegarde l'information dans la base de donnée.
    Retourne à l'utilisateur si elle est bissextile ou non.
    """
    # On teste si l'année en entrée est bissextile ou non
    is_bis = est_bissextile(annee)
    # On enregistre dans la base de données
    objet_annee = Bissextile.objects.create(annee=annee, is_bissextile=is_bis,
                                            endpoint_utilise="Bissextile")
    # On affiche le bon message
    if objet_annee.is_bissextile:
        return f"L'année {annee} est bissextile."
    return f"L'année {annee} n'est pas bissextile."


@api.post('/bissextile/range/{annee_debut}and{annee_fin}')
def rangea(request, annee_debut: int, annee_fin: int) -> str:
    """
    Prend en entrée un intervalle d'année.
    Regarde toutes les années bissextiles entre ces deux années.
    Sauvegarde l'information dans la basse de donnée.
    Retourne à l'utilisateur toutes les années bissextile.
    """
    annee_debut_iterable: int = annee_debut
    # liste pour stocker les années bissextiles et pouvoir les retourner à l'utilisateur
    liste_annees = []
    # On parcourt tous les années et on regarde si elles sont bissextiles pour les ajouter ou non à la liste que l'on renvoie à l'utilisateur
    for _ in range(annee_fin - annee_debut_iterable + 1):
        if est_bissextile(annee_debut_iterable):
            liste_annees.append(annee_debut_iterable)
        annee_debut_iterable += 1
    # On convertit notre liste en chaine de charactère pour l'enregistrer et l'afficher sans les []
    liste_annees = str(liste_annees)[1:-1]
    # On sauvegarde dans la base de données
    Bissextile.objects.create(annee_debut=annee_debut,
                              annee_fin=annee_fin, annees_bissextiles=liste_annees,
                              endpoint_utilise="Range")
    return f"Les années {liste_annees} sont bissextiles."


@api.get('/bissextile/history')
def history(request) -> dict[int, dict[str, Any]]:
    """
    Permet de donner l'historique des requêtes effectués ainsi que la sortie de celles-ci
    Rangé par date de création croissante
    """
    objet = Bissextile.objects.all()
    affichage = {}
    i = 1
    for truc in objet:
        affichage[i] = {"id": truc.id, "endpoint_utilise": truc.endpoint_utilise, "annee": truc.annee,
                        "is_bissextie": truc.is_bissextile,
                        "annee_debut": truc.annee_debut, "annee_fin": truc.annee_fin,
                        "annees_bissextiles": truc.annees_bissextiles,
                        "created_at": truc.created_at, "updated_at": truc.updated_at}
        i += 1
    return affichage
