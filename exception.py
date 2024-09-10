# Fichier: gestion_erreurs.py
# Ce fichier contient des exemples d'utilisation de try, except, else, et finally en Python

def exemple_division():
    """
    Exemple 1: Division avec gestion d'erreurs
    Démontre la gestion des erreurs de division par zéro et de saisie invalide.
    """
    try:
        # Le bloc try contient le code susceptible de générer une exception
        numerateur = int(input("Entrez le numérateur : "))
        denominateur = int(input("Entrez le dénominateur : "))
        resultat = numerateur / denominateur
    except ZeroDivisionError:
        # Ce bloc s'exécute si une division par zéro est détectée
        print("Erreur : Division par zéro impossible!")
    except ValueError:
        # Ce bloc s'exécute si la conversion en int échoue
        print("Erreur : Veuillez entrer des nombres valides.")
    else:
        # Le bloc else s'exécute si aucune exception n'est levée dans le try
        print(f"Le résultat de la division est : {resultat}")
    finally:
        # Le bloc finally s'exécute toujours, qu'une exception soit levée ou non
        print("Opération de division terminée.")


def exemple_lecture_fichier():
    """
    Exemple 2: Lecture de fichier avec gestion d'erreurs
    Démontre la gestion des erreurs lors de l'ouverture et de la lecture d'un fichier.
    """
    nom_fichier = "exemple.txt"
    try:
        with open(nom_fichier, 'r') as fichier:
            contenu = fichier.read()
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except IOError:
        print(f"Erreur : Problème lors de la lecture du fichier '{nom_fichier}'.")
    else:
        print(f"Contenu du fichier '{nom_fichier}' :")
        print(contenu)
    finally:
        print("Tentative de lecture du fichier terminée.")


def exemple_conversion_type():
    """
    Exemple 3: Conversion de type avec gestion d'erreurs
    Démontre la gestion des erreurs lors de la conversion de chaînes en nombres.
    """
    valeurs = ["10", "20", "trente", "40.5", "50"]

    for val in valeurs:
        try:
            nombre = int(val)
        except ValueError:
            try:
                nombre = float(val)
            except ValueError:
                print(f"Impossible de convertir '{val}' en nombre.")
            else:
                print(f"Converti en float : {nombre}")
        else:
            print(f"Converti en int : {nombre}")
        finally:
            print(f"Traitement de '{val}' terminé.")
        print("-" * 20)


def exemple_court_multiple_exceptions():
    """
    Exemple court : Gestion de plusieurs exceptions dans un seul bloc except
    """
    valeurs = [10, 0, "abc", []]

    for val in valeurs:
        try:
            resultat = 100 / val
            print(f"100 / {val} = {resultat}")
        except (TypeError, ZeroDivisionError) as e:
            print(f"Erreur avec {val}: {type(e).__name__}")  # Renvoie la classe avec type(e), nom de la classe sous forme de chaine avec __name__


# Exécution des exemples
if __name__ == "__main__":
    # print("Exemple 1: Division")
    # exemple_division()
    # print("\nExemple 2: Lecture de fichier")
    # exemple_lecture_fichier()
    # print("\nExemple 3: Conversion de type")
    # exemple_conversion_type()
    print("\nExemple 4: Multiples exceptions")
    exemple_court_multiple_exceptions()