#Troy Tural
#GR:404
#EXCERSICE POO#3

import random

#Puisqu`il faut lancer 4 dées aleatoires de 1 à 6, on doit crée un def pour effectuer les 4 lancers
def lancer():
   lancer1 = random.randint(1,6)
   lancer2 = random.randint(1,6)
   lancer3 = random.randint(1,6)
   lancer4 = random.randint(1,6)

#Les valeures choisis vont êtres par les 3 plus grandes valeurs des 4 lancers de dées, donc il faut assuer de crée un if pour chaque lancer
   if lancer1 < lancer2 and lancer1 < lancer3 and lancer1 < lancer4:
       lancer = lancer2 + lancer3 + lancer4
       return lancer

   if lancer2 < lancer1 and lancer2 < lancer3 and lancer2 < lancer4:
       lancer = lancer1 + lancer3 + lancer4
       return lancer

   if lancer3 < lancer1 and lancer3 < lancer2 and lancer3 < lancer4:
       lancer = lancer1 + lancer2 + lancer4
       return lancer

   if lancer4 < lancer1 and lancer4 < lancer2 and lancer4 < lancer3:
       lancer = lancer1 + lancer2 + lancer3
       return lancer


#Il faut qu`on crée une classe NPC qui va faire heriter ses donnés par la classe Kobold et la classe HERO.
#Ceratines varibles des selfs vont dependre de la somme de 3 des 4 lancers. Ces variables vont etre marquées par "lancer()"
class NPC:
    def __init__(self,name):
       self.ATK = lancer()
       self.AGI = lancer()
       self.CONS = lancer()
       self.INT = lancer()
       self.SAGE = lancer()
       self.CARI = lancer()
       self.DEF = random.randint(1,12)
       self.NAME = ('Eddie')
       self.RACE = ('Human')
       self.HP = (20)
       self.JOB = ('Geomancer')
#Ceci va faire en sore que lorsque le code est effectuer, la console va afficher les caractéristiques du NPC
    def afficher_NPC(self):
        print()

#La classe Kobold va hériter de la classe NPC
class Kobold(NPC):
    def attack(self,cible):#Ces 2 lignes sont ceux qui definissent la force d`attaque du Kobold
        return random.randint(1, 6) + self.ATK

#Cette ligne est celui qui calcul le montant de dommage que le Kobold peut recevoir par une attaque
    def damage_taken(self,dmg):
        self.HP -= dmg - self.DEF

#la classe HERO va aussi heriter les caractéristiqes du NPC(ATK,DEF,INT,etc)
class HERO(NPC):
    def attack(self,cible):
        #Cette ligne va faire en sorte qui si le resultat du lancer de 1 DÉE est egale exactement a 20, la classe HERO effectura une attaque critique qui est garantie de toucher sa cible qui s`agit du Kobold
        lancer = random.randint(1, 20)
        if lancer == 20:
            #Puisque l`attaque est garantie de faire contact avec sa cible, le Kobold prendre un nombre aleatoire de dommages de 1 à 8
            cible.HP -= random.randint(1, 8)
#Si le lancer de dée est exactement 1, la cible va eviter l`attaque. Donc le Kobold ne prendra pas de dommages
        if lancer == 1:
            cible.HP -= 0
#Si le lancer du déée est plus grand que la defense de la cible, le Kobold perdera un nombre aléatoir de dommages de 1 à 6
        if lancer > cible.DEF:
            cible.HP -= random.randint(1,6)
#Si le lancer du dée est egale à moins que la defense de la cible, le Kobold ne prendra pas de dommages.
        if lancer < cible.DEF:
            cible.HP -= 0












