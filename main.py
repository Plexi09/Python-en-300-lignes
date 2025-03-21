#################################################################################
#           PYTHON EN MOINS DE 300 LIGNES | FAIT AVEC ❤ PAR PLEXI09            #
#################################################################################

# Ceci est un commentaire, il est ignoré par l'interpréteur. Vous pouvez l'utiliser pour écrire des notes pour vous-même ou pour d'autres.

# VARIABLES

# Définir une variable
foo = 0 # Nous définissons une variable de type INT, foo est égal (=) à 0

# Nous pouvons ajouter à cette variable en utilisant l'opérateur +=, cela fonctionne aussi pour les chaînes de caractères.
foo += 1 # foo vaut maintenant 1

# Nous pouvons aussi soustraire à cette variable en utilisant l'opérateur -=
foo -= 1 # foo vaut maintenant 0, car avant il était à 1

# Maintenant, foo est un tableau (liste). Nous pouvons ajouter des éléments avec la méthode append()
foo = [] # foo est maintenant une liste

foo.append(1) # foo vaut maintenant [1]
foo[0] += 1 # foo vaut maintenant [2], car nous avons sélectionné le premier élément de la liste et ajouté 1.

# Les listes peuvent contenir d'autres listes, on appelle cela un tableau multidimensionnel. Cela est utile pour stocker des données sous forme de grille.
foo2 = [[1, 2], [3, 4]] # foo2 est maintenant un tableau multidimensionnel

print(foo2[0][0]) # Cela affichera 1, car nous sélectionnons le premier élément de la première liste dans foo2.


# FONCTIONS

def multiplier_par_deux(nombre): # Définition d'une fonction qui prend un nombre en argument
    return nombre * 2 # Retourne le nombre multiplié par 2


# CONDITIONS ET BOUCLES

foo = 6 # foo vaut maintenant 6

if foo > 5: # Si foo est supérieur à 5
    print("foo est supérieur à 5")
else:
    print("foo n'est pas supérieur à 5")

# Opérateurs de comparaison : >, <, >=, <=, ==, != (supérieur, inférieur, supérieur ou égal, inférieur ou égal, égal, différent)
# Opérateurs logiques : and, or, not

foo = [1, 2, 3, 4, 5]

if (3 in foo and len(foo) == 5) or foo[4] == 5:
    print("Les conditions sont remplies")

# Boucle for pour parcourir une liste
for nombre in foo:
    print(nombre)

# Boucle while
foo = 0
while foo < 5:
    print(foo)
    foo += 1

# Utilisation de break et continue
foo = 0
while True:
    if foo == 5:
        break
    print(foo)
    foo += 1

# CLASSES

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans")

personne = Personne("Jean", 30)
personne.saluer()

# EXCEPTIONS

try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro")

# EXERCICES
# 🟢 - Facile
# 🔵 - Moyen
# 🔴 - Difficile

# 🟢 1. Écrire une fonction qui prend un nombre et retourne son carré.
# 🔵 2. Compléter le code suivant pour afficher tous les nombres pairs de 1 à 10.
# for nombre in range(1,    ):
#     if nombre % 2 == 0:
#         print(           )

# 🔵 5. Écrire une classe Cercle avec un attribut rayon et une méthode aire() retournant l'aire du cercle.

# Bonne chance ! 🚀
