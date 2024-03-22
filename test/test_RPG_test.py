import unittest

from src.personnage import Personnage


class MyTestCase(unittest.TestCase):

    def test_initial_hp(self):
        personnage = Personnage()
        self.assertEqual(100, personnage.get_point_de_vie())  # add assertion here

    def test_est_mort(self):
        personnage = Personnage()
        personnage.tuer()
        self.assertEqual(0, personnage.get_point_de_vie())
        self.assertTrue(True, personnage.est_mort())

    def test_initialement_vivant(self):
        personnage = Personnage()
        self.assertFalse(personnage.est_mort())

    def test_attaque(self):
        attaquant = Personnage()
        attaque = Personnage()
        attaquant.attaque(attaque, 5)
        self.assertEqual(100, attaquant.get_point_de_vie())
        self.assertLess(attaque.get_point_de_vie(), 100)

    def test_attaque_mortelle(self):
        attaquant = Personnage()
        attaque = Personnage()
        attaquant.attaque(attaque, 98)
        attaquant.attaque(attaque, 2)
        self.assertEqual(100, attaquant.get_point_de_vie())
        self.assertEqual(0, attaque.get_point_de_vie())

    def test_point_de_vie_non_negatif(self):
        attaquant = Personnage()
        attaque = Personnage()
        attaquant.attaque(attaque, 98)
        attaquant.attaque(attaque, 5)
        self.assertEqual(100, attaquant.get_point_de_vie())
        self.assertEqual(0, attaque.get_point_de_vie())

    def test_defense(self):
        attaquant = Personnage()
        attaque = Personnage()
        attaque.defend()
        before_attack = attaque.get_point_de_vie()
        attaquant.attaque(attaque, 98)
        after_attack = attaque.get_point_de_vie()
        self.assertEqual(before_attack, after_attack)

    def test_defense_disabled(self):
        attaquant = Personnage()
        attaque = Personnage()
        attaque.defend()
        attaquant.attaque(attaque, 1)
        attaquant.attaque(attaque, 10)
        self.assertEqual(90, attaque.get_point_de_vie())


if __name__ == '__main__':
    unittest.main()
