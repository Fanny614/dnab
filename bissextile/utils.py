def est_bissextile(annee:int) -> bool:
    """
    :param annee:
    :return: True / False

    Prend en une année en entrée
    Retourne True ou False pour dire si l'année et bissextile ou non
    """
    if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
        return True
    return False
