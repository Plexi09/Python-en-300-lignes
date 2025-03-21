#################################################################################
#           PYTHON EN 300 LIGNES | FAIT AVEC ❤ PAR PLEXI09            #
#################################################################################

# COMMENTAIRES

# Un commentaire en Python commence par un dièse (#). 
# Tout texte qui suit ce symbole est ignoré par l'interpréteur Python.
# Les commentaires permettent de rendre le code plus compréhensible pour l'humain et expliquent son fonctionnement.

# VARIABLES

# Une variable est un conteneur qui permet de stocker une valeur en mémoire.
# Cette valeur peut être un entier, une chaîne de caractères, une liste, etc.
example = 0  # On déclare une variable 'example' de type entier (INT) avec une valeur initiale de 0.

# L'opérateur += permet d'incrémenter la valeur d'une variable.
example += 1  # La variable 'example' est incrémentée de 1, passant de 0 à 1.

# De même, l'opérateur -= permet de décrémenter la valeur de la variable.
example -= 1  # La variable 'example' est décrémentée de 1, revenant à 0.

# Une liste est une structure de données qui permet de stocker plusieurs valeurs sous un même nom.
# Ces valeurs peuvent être de types différents (entiers, chaînes de caractères, etc.).
example = []  # On déclare une liste vide.

# La fonction append() permet d'ajouter un élément à la fin de la liste.
example.append(1)  # L'élément 1 est ajouté à la liste. La liste devient [1].

# Accéder à un élément d'une liste se fait en utilisant son index (commençant à 0).
# Par exemple, example[0] accédera au premier élément de la liste.
example[0] += 1  # L'élément à l'index 0 (qui vaut 1) est incrémenté de 1. La liste devient [2].

# Une liste peut contenir d'autres listes, formant ainsi une structure imbriquée, appelé matrice.
example2 = [[1, 2], [3, 4]]  # Déclaration d'une matrice 2x2 contenant des listes imbriquées.

# Accéder à un élément d'une liste imbriquée :
print(example2[0][0])  # Accède au premier élément de la première liste imbriquée, donc 1.

# FONCTIONS

# Une fonction est un bloc de code réutilisable. Elle prend généralement des arguments en entrée et retourne un résultat.
# L'avantage des fonctions est d'éviter la répétition du même code plusieurs fois.

def multiplier_par_deux(nombre):  # La fonction prend un argument 'nombre'.
    return nombre * 2  # Elle retourne ce nombre multiplié par 2.

# Exemple d'utilisation de la fonction :
resultat = multiplier_par_deux(4)  # On passe l'argument 4 à la fonction, qui retourne 4 * 2 = 8.
print(resultat)  # Affiche 8.

# CONDITIONS ET BOUCLES

# Les conditions permettent d'exécuter un bloc de code uniquement si une certaine condition est vraie.

example = 6  # On assigne la valeur 6 à la variable 'example'.

# Structure conditionnelle 'if' : si la condition est vraie, le code à l'intérieur du bloc est exécuté.
if example > 5:  # Teste si 'example' est supérieur à 5.
    print("example est supérieur à 5")  # Si la condition est vraie, affiche ce message.
else:
    print("example n'est pas supérieur à 5")  # Si la condition est fausse, affiche ce message.

# Une boucle 'for' permet de parcourir une séquence (comme une liste) et d'exécuter un bloc de code pour chaque élément.
example = [1, 2, 3, 4, 5]
for nombre in example:
    print(nombre)  # Affiche chaque élément de la liste 'example' un par un.

# Une boucle 'while' s'exécute tant que la condition spécifiée reste vraie.
example = 0
while example < 5:  # Tant que 'example' est inférieur à 5 :
    print(example)  # Affiche la valeur actuelle de 'example'.
    example += 1  # Incrémente 'example' de 1 à chaque itération.

# CLASSES

# Une classe est un modèle pour créer des objets avec des propriétés et des méthodes associées.
# Un objet est une instance d'une classe, et il possède ses propres valeurs pour ces propriétés.
class Personne:
    def __init__(self, nom, age):  # Le constructeur est appelé lors de la création d'un objet. 
        self.nom = nom  # La propriété 'nom' est initialisée avec la valeur donnée.
        self.age = age  # La propriété 'age' est initialisée avec la valeur donnée.

    def saluer(self):  # Une méthode qui fait saluer la personne.
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans")  # Affiche un message de salutation.

# On crée une instance de la classe 'Personne' en passant 'Jean' et 30 comme valeurs pour 'nom' et 'age'.
personne = Personne("Jean", 30)
personne.saluer()  # Affiche "Bonjour, je m'appelle Jean et j'ai 30 ans".

# EXCEPTIONS

# Les exceptions permettent de gérer les erreurs qui se produisent pendant l'exécution du programme.
# En cas d'erreur, l'exécution normale du programme est interrompue, mais on peut gérer cette erreur avec 'try' et 'except'.

try:
    resultat = 10 / 0  # Cette ligne provoque une erreur de division par zéro.
except ZeroDivisionError:  # Si une erreur de type 'ZeroDivisionError' est levée, le code dans ce bloc est exécuté.
    print("Erreur : division par zéro")  # Affiche un message d'erreur expliquant le problème.

# EXERCICES

# 🟢 1. Fonction retournant le carré d'un nombre.
def carre(nombre):
    return nombre ** 2  # La fonction retourne le carré du nombre en utilisant l'opérateur '**' pour l'exponentiation.

# 🔵 2. Afficher tous les nombres pairs de 1 à 10.
for nombre in range(1, 11):  # La fonction range génère des nombres de 1 à 10 (11 exclu).
    if nombre % 2 == 0:  # Si le nombre est divisible par 2, il est pair.
        print(nombre)  # Affiche les nombres pairs.

# 🔵 3. Fonction pour vérifier si un nombre est premier.
def est_premier(nombre):
    if nombre < 2:  # Les nombres inférieurs à 2 ne sont pas premiers.
        return False
    for i in range(2, nombre):  # On teste si le nombre est divisible par un autre nombre que 1 et lui-même.
        if nombre % i == 0:  # Si le nombre est divisible par 'i', il n'est pas premier.
            return False
    return True  # Si aucune division n'a eu lieu, le nombre est premier.

# 🔵 4. Calcul de la factorielle d'un nombre.
def factorielle(n):
    if n == 0:  # Par définition, la factorielle de 0 est 1.
        return 1
    resultat = 1
    for i in range(1, n + 1):  # On multiplie tous les nombres de 1 à n.
        resultat *= i
    return resultat

# 🔵 5. Classe Cercle avec calcul de l'aire.
import math  # On importe le module math pour utiliser la constante pi.

class Cercle:
    def __init__(self, rayon):  # Le constructeur prend un argument 'rayon' pour définir le rayon du cercle.
        self.rayon = rayon  # La propriété 'rayon' est initialisée avec la valeur donnée.

    def aire(self):  # Méthode pour calculer l'aire du cercle.
        return math.pi * self.rayon ** 2  # L'aire d'un cercle est donnée par la formule : pi * r^2.

# On crée un objet de la classe Cercle avec un rayon de 5.
cercle1 = Cercle(5)
print(f"L'aire du cercle est : {cercle1.aire()}")  # Affiche l'aire du cercle avec le rayon 5.

# 🟢 6. Inverser une chaîne de caractères.
def inverser_chaine(chaine):
    return chaine[::-1]  # Utilise le "slicing" pour inverser la chaîne.

# 🟢 7. Vérifier si un mot est un palindrome.
def est_palindrome(mot):
    return mot == mot[::-1]  # Vérifie si le mot est égal à son inverse.

# Bonne chance ! 🚀
