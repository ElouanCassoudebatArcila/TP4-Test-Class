"""
Elouan Cassoudebat--Arcila,407
exercice pour apprendrea utiliser les classes
"""
from math import pi
from random import randint
from dataclasses import dataclass


# 1

class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(f"{self.message.upper()}")


Charles = StringFoo(message="Charle deguire et pa bo")
Charles.print_string()


# 2

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calcul_aire(self):
        return self.longueur * self.largeur

    def afficher_infos(self):
        print(self.longueur, self.largeur, self.calcul_aire())


rectangle = Rectangle(longueur=10, largeur=5)
rectangle.afficher_infos()


# 3

class Cercle:
    def __init__(self, rayon, ):
        self.rayon = rayon

    def calcul_aire(self):
        return self.rayon * self.rayon * pi

    def calcul_circonference(self):
        return self.rayon * 2 * pi

    def afficher_infos(self):
        print(self.calcul_aire(), self.calcul_circonference())


cercle = Cercle(rayon=6)
cercle.afficher_infos()


# 4

class Hero:
    def __init__(self, pv, force_attaque, force_defense, nom_hero):
        self.dommage = None
        self.pv = randint(1, 10) + randint(1, 10)
        self.force_attaque = randint(1, 6)
        self.force_defense = randint(1, 6)
        self.nom_hero = nom_hero

    def faire_une_attaque(self):
        return randint(1, 6) + self.force_attaque

    def recevoir_dommage(self, dommage):
        self.dommage = dommage
        self.pv -= self.dommage - self.force_defense

    def est_vivant(self):
        return self.pv > 0


# 5

def de():
    return randint(1, 20)


@dataclass
class Caracteristique:
    force: int = de()
    dexterite: int = de()
    constitution: int = de()
    intelligence: int = de()
    sagesse: int = de()
    charisme: int = de()

# 6


class Hero2:
    def __init__(self, nom_hero):
        self.dommage = None
        self.pv = randint(1, 10) +randint(1, 10)
        self.force_attaque = randint(1, 6)
        self.force_defense = randint(1, 6)
        self.nom_hero = nom_hero
        self.caracteristique = Caracteristique()

    def faire_une_attaque(self):
        return randint(1, 6) + self.force_attaque

    def recevoir_dommage(self, dommage):
        self.dommage = dommage
        self.pv -= self.dommage + self.force_defense

    def est_vivant(self):
        return self.pv > 0


h = Hero2("Elouan")
print(h.__dict__)
