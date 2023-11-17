# Import du framework de tests unitaires unittest
import unittest
import calc


class Test(unittest.TestCase):
    """
    Tests pour les fonctions de calc
    """

    # Test du périmètre d'un rectangle
    def test_perimetre_rectangle(self):
        # Test avec des données valides
        self.assertEqual(calc.perimetre_rectangle(10, 20), 60)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.perimetre_rectangle, -1, 0)

    # Test de la surface d'un rectangle
    def test_surface_rectangle(self):
        # Test avec des données valides
        self.assertEqual(calc.surface_rectangle(10, 20), 200)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.surface_rectangle, -1, 0)

    # Test du périmètre d'un cercle
    def test_perimetre_cercle(self):
        # Test avec des données valides
        self.assertEqual(calc.perimetre_cercle(1), 2 * 3.14159)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.perimetre_cercle, -1)

    # Test de la surface d'un cercle
    def test_surface_cercle(self):
        # Test avec des données valides
        self.assertEqual(calc.surface_cercle(1), 3.14159)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.surface_cercle, -1)

    # Test du périmètre d'un triangle
    def test_perimetre_triangle(self):
        # Test avec des données valides
        self.assertEqual(calc.perimetre_triangle(10, 20, 30), 60)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.perimetre_triangle, 0, 0, 0)

    # Test de la surface d'un triangle
    def test_surface_triangle(self):
        # Test avec des données valides
        self.assertEqual(calc.surface_triangle(10, 20), 100)

        # Test avec des données invalides
        self.assertRaises(ValueError, calc.surface_triangle, 0, 0)

if __name__ == "__main__":
    unittest.main()
