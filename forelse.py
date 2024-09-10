"""
Le bloc "for-else" en Python est une structure qui permet d'exécuter un code spécifique si la boucle "for" se termine
normalement, c'est-à-dire sans rencontrer d'instruction "break".
"""


def chercher_nombre_pair(liste):
    for nombre in liste:
        if nombre % 2 == 0:
            print(f"Nombre pair trouvé : {nombre}")
            break
    else:
        print("Aucun nombre pair n'a été trouvé dans la liste.")


# Exemple d'utilisation
liste1 = [1, 3, 5, 7, 9]
liste2 = [1, 3, 4, 7, 9]

chercher_nombre_pair(liste1)
chercher_nombre_pair(liste2)
