"""
Un script python prenant 3 arguments dont le premier est l'opération voulue et les deux suivants
les deux entiers
"""

import calc
import sys

print("Bienvenue dans ce petit programme sous Python permet de calculer le périmètre et la surface d'une forme géométrique.\n")


def main_calc():

    # Menu principal
    print("1. Calculer le périmètre et la surface d'un rectangle")
    print("2. Calculer le périmètre et la surface d'une cercle")
    print("3. Calculer le périmètre et la surface d'un triangle")
    print("4. Quitter")

    # Choix de l'utilisateur
    choix = input("Votre choix : \n")

    # Traitement du choix
    if choix == "1":
        # Saisie des dimensions du rectangle
        largeur = float(input("Largeur du rectangle : \n"))
        longueur = float(input("Longueur du rectangle : \n"))

        # Calcul du périmètre et de la surface
        perimetre = calc.perimetre_rectangle(largeur, longueur)
        surface = calc.surface_rectangle(largeur, longueur)

        # Affichage des résultats
        print("Périmètre du rectangle :", perimetre)
        print("Surface du rectangle :", surface)

    elif choix == "2":
        # Saisie du rayon du cercle
        rayon = float(input("Rayon du cercle : \n"))

        # Calcul du périmètre et de la surface
        perimetre = calc.perimetre_cercle(rayon)
        surface = calc.surface_cercle(rayon)

        # Affichage des résultats
        print("Périmètre du cercle :", perimetre)
        print("Surface du cercle :", surface)

    elif choix == "3":
        # Saisie des longueurs des côtés du triangle
        côté_a = float(input("Longueur du côté a du triangle : \n"))
        côté_b = float(input("Longueur du côté b du triangle : \n"))
        côté_c = float(input("Longueur du côté c du triangle : \n"))

        # Calcul du périmètre et de la surface
        perimetre = calc.perimetre_triangle(côté_a, côté_b, côté_c)
        surface = calc.surface_triangle(côté_a, côté_b)

        # Affichage des résultats
        print("Périmètre du triangle :", perimetre)
        print("Surface du triangle :", surface)

    elif choix == "4":
        # Quitter le programme
        print("Au revoir !\n")
    else:
        # Choix invalide
        print("Choix invalide.\n")

    print("Nous allons recommencer le programme\n")
    main_calc()

if __name__ == "__main__":
    main_calc()
