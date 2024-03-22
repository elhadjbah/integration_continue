from dataclasses import dataclass
from random import randint

@dataclass
class Personnage:
    _points_de_vie: int = 100
    _mort: bool = False
    _en_defense: bool = False

    def est_mort(self):
        return self._mort

    def get_point_de_vie(self):
        return self._points_de_vie

    def defend(self):
        self._en_defense = True

    def get_defense(self):
        return self._en_defense

    def not_defending(self):
        self._en_defense = False

    def subit_attaque(self, point_perdu: int):
        if self._points_de_vie - point_perdu >= 0:
            self._points_de_vie -= point_perdu
        else:
            self.tuer()

    def attaque(self, other: 'Personnage', puissance: int):
        if not other.get_defense():
            other.subit_attaque(puissance)
        other.not_defending()

    def tuer(self):
        self._points_de_vie = 0
        self._mort = True

