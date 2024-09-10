"""
EAFP : Easier to Ask for Forgiveness than Permission
Traduction : Il est plus facile de demander pardon que la permission
Signification : Supposer que les opérations vont réussir et gérer les exceptions si elles se produisent.

LBYL : Look Before You Leap
Traduction : Regarder avant de sauter
Signification : Vérifier les conditions avant d'effectuer une opération.

En Python, l'approche EAFP est généralement préférée car elle produit souvent
un code plus lisible et plus efficace, en particulier dans les situations où
les exceptions sont rares.
"""

personne = {"nom": "Dupont", "age": 30}

# EAFP (Easier to Ask for Forgiveness than Permission)
def get_age_eafp(dict_personne):
    try:
        return f"Age: {dict_personne['age']}"
    except KeyError:
        return "Age non spécifié"

# LBYL (Look Before You Leap)
def get_age_lbyl(dict_personne):
    if 'age' in dict_personne:
        return f"Age: {dict_personne['age']}"
    else:
        return "Age non spécifié"

# Test
print("EAFP:", get_age_eafp(personne))
print("LBYL:", get_age_lbyl(personne))

# Test avec une clé manquante
personne_sans_age = {"nom": "Martin"}
print("EAFP (clé manquante):", get_age_eafp(personne_sans_age))
print("LBYL (clé manquante):", get_age_lbyl(personne_sans_age))