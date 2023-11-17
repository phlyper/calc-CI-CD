"""
La librairie calc permet de faire les opérations de calcul perimetre et surface.
"""

def perimetre_rectangle(largeur, longueur):
  return 2 * (largeur + longueur)

def surface_rectangle(largeur, longueur):
  return largeur * longueur

def perimetre_cercle(rayon):
  return 2 * 3.14159 * rayon

def surface_cercle(rayon):
  return 3.14159 * rayon ** 2

def perimetre_triangle(côté_a, côté_b, côté_c):
  return côté_a + côté_b + côté_c

def surface_triangle(base, hauteur):
  return (base * hauteur) / 2
