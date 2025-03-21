#################################################################################
#               PYTHON EN 340 LIGNES | FAIT AVEC ❤ PAR PLEXI09                 #
#################################################################################

# INTRODUCTION

# Bienvenue dans "Python en 340 lignes" !
# Ce tutoriel vous permettra de découvrir les bases de la programmation en Python en exactement 340 lignes de code.
# Il couvre les concepts fondamentaux tels que les variables, les fonctions, les conditions, les boucles, les classes et les exceptions.
# Chaque section est accompagnée d'exemples pratiques et d'exercices pour tester vos connaissances.
# Je vous encourage à lire attentivement chaque section, à exécuter le code et à résoudre les exercices proposés.
# Si vous lisez ce guide sur le site github.com, les commentaires sont en gris et les exemples de code en couleur.

# Python est un langage de programmation de haut niveau, c'est a dire proche du langage humain, créé par Guido van Rossum et publié en 1991. Il se distingue par :
# - Sa simplicité et sa lisibilité
# - Sa grande polyvalence (web, data science, IA, scripts systèmes...)
# - Sa vaste bibliothèque standard
# - Sa communauté active et son écosystème riche
# - Son adoption par de nombreuses entreprises et universités
# - Son interpréteur interactif (REPL) pour tester du code en temps réel
#
# Python est un langage interprété, ce qui signifie que le code est exécuté ligne par ligne de haut en bas par un interpréteur Python,
# a l'inverse d'un langage compilé comme Java qui est traduit d'une traite en langage machine par le compilateur.

# Entreprises et organisations utilisant Python :
# - Google (YouTube, Search)
# - Facebook (Instagram)
# - Netflix
# - Spotify
# - Dropbox
# - NASA
# - CERN

# Domaines d'application de Python :
# - Développement web (Django, Flask)
# - Data science (Pandas, NumPy, Matplotlib)
# - Intelligence artificielle (TensorFlow, PyTorch)
# - Automatisation (scripts, bots)
# - Jeux vidéo (Pygame)
# - Systèmes embarqués (MicroPython)
# - Enseignement et recherche

# Cette introduction a pour objectifs de :
# 1. Présenter les concepts fondamentaux de Python
# 2. Fournir des exemples pratiques et commentés
# 3. Permettre une prise en main rapide du langage
# 4. Proposer des exercices pour s'entraîner

# TERMINOLOGIE

# Voici quelques termes courants en programmation Python (et en informatique en général) :

# - Interpréteur : un programme qui exécute du code Python ligne par ligne. (A ne pas confondre avec un compilateur ou un environnement de développement.)
# - Module : un fichier contenant des fonctions et des variables. (Exemple : math, random)
# - Bibliothèque : un ensemble de modules. (Exemple : bibliothèque standard de Python)
# - Chaîne de caractères : une séquence de caractères (texte) entre guillemets simples ou doubles. (Exemple : "Bonjour")
# - Entier : un nombre entier sans décimales. (Exemple : 42)
# - Flottant : un nombre à virgule (nombre réel). (Exemple : 3.14)
# - Booléen : une valeur logique (True ou False).
# - Opérateur : un symbole pour effectuer une opération (comme +, -, *, /).
# - Fonction standard : une fonction fournie par Python (comme print() ou len()).
# - Module standard : un module fourni par Python (comme math ou random).
# - Constante : une valeur qui ne change pas (comme math.pi).
# - Importer : inclure un module dans un script Python. (Exemple : import math)
# - Argument : une valeur fournie à une fonction ou un script. (Exemple : print("Bonjour"))
# - Exécuter : lancer un script ou un programme. (Exemple : python script.py)
# - Variable : un conteneur pour stocker des données. (Exemple : x = 42)
# - Fonction : un bloc de code réutilisable. (Exemple : def ma_fonction():)
# - Condition : une instruction pour exécuter du code sous certaines conditions. (Exemple : if x > 5:)
# - Boucle : une structure pour répéter une action. (Exemple : for i in range(5):)
# - Classe : un modèle pour créer des objets. (Exemple : Personne, Voiture)
# - Objet : une instance d'une classe. (Exemple : Jean est une instance de la classe Personne)
# - Propriété : une caractéristique d'un objet. (Exemple : nom, age)
# - Méthode : une fonction associée à un objet.
# - Exception : une erreur qui interrompt l'exécution du programme. (Exemple : ZeroDivisionError)
# - Liste : une structure de données pour stocker plusieurs éléments. (Exemple : [1, 2, 3])
# - Index : la position d'un élément dans une liste (commençant à 0). (Exemple : liste[0])

# Maintenant que vous avez aquis le vocabulaire de base, passons aux concepts fondamentaux de Python !


####################
# LES COMMENTAIRES #
####################


# Un commentaire en Python commence toujours par un dièse (#). 
# Tout texte qui suit ce symbole est ignoré par l'interpréteur Python.
# Les commentaires permettent de rendre le code plus compréhensible pour l'humain et expliquent son fonctionnement.

# LES VARIABLES

# Une variable est un conteneur qui permet de stocker une valeur en mémoire.
# Cette valeur peut être un entier, une chaîne de caractères, une liste, etc.
# Le nom d'une variable est arbitraire, mais doit commencer par une lettre ou un underscore (_)
# et ne pas contenir d'espaces ou de caractères spéciaux (Exemple: é, $, %).
# Les noms de variables sont sensibles à la casse (majuscules/minuscules).
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

# Une liste peut contenir d'autres listes, formant ainsi une structure imbriquée, appelée matrice.
example2 = [[1, 2], [3, 4]]  # Déclaration d'une matrice 2x2 contenant des listes imbriquées.

# Accéder à un élément d'une liste imbriquée :
print(example2[0][0])  # Accède au premier élément de la première liste imbriquée, donc 1.


####################
# LES FONCTIONS    #
####################

# Une fonction est un bloc de code réutilisable. Elle prend généralement des arguments en entrée et retourne un résultat.
# L'avantage des fonctions est d'éviter la répétition du même code plusieurs fois.
# Une fonction est définie par le mot-clé 'def', suivi du nom de la fonction et de ses paramètres entre parenthèses.
# Le code de la fonction est indenté (décalé) pour indiquer qu'il fait partie de la fonction.
# La valeur de retour d'une fonction est définie par l'instruction 'return'.
# Les fonctions peuvent être appelées (exécutées) en utilisant leur nom suivi de parenthèses contenant les arguments.
# Les arguments sont les valeurs que la fonction utilise pour effectuer ses calculs.
# Par convention, les noms de fonctions commencent par une minuscule et les mots sont séparés par des underscores (_).

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

# La fonction range() génère une séquence de nombres.
# Par exemple, range(5) génère les nombres de 0 à 4 (5 exclu).
for i in range(5):
    print(i)  # Affiche les nombres de 0 à 4 car la boucle se répète 5 fois.

# Une boucle 'while' s'exécute tant que la condition spécifiée reste vraie.
example = 0
while example < 5:  # Tant que 'example' est inférieur à 5 :
    print(example)  # Affiche la valeur actuelle de 'example'.
    example += 1  # Incrémente 'example' de 1 à chaque itération.

# On peut combiner les boucles et les conditions pour créer des structures de contrôle plus complexes.
for i in range(10): # aka pour chaque nombre de 0 à 9
    if i % 2 == 0:  # Si 'i' est pair :
        print(i, " est pair")  # Affiche que 'i' est pair.
    else:
        print(i, " est impair")  # Sinon, affiche que 'i' est impair.

# On peut utiliser l'instruction 'break' pour sortir d'une boucle prématurément.
example = 0
while True:  # Boucle infinie.
    print(example)
    example += 1 # Incrémente 'example' de 1 à chaque itération.
    if example >= 5:  # Si 'example' est supérieur ou égal à 5 :
        break  # Sort de la boucle.
# Cette boucle affiche les nombres de 0 à 4, puis s'arrête.

# On peut utiliser l'instruction 'continue' pour passer à l'itération suivante d'une boucle.
for i in range(5):
    if i == 3:  # Si 'i' est égal à 3 :
        continue  # Passe à l'itération suivante sans exécuter le code restant.
    print(i)  # Affiche les nombres de 0 à 4, sauf 3.

####################
# LES CLASSES      #
####################

# Une classe est un modèle pour créer des objets avec des propriétés et des méthodes associées.
# Par convention, les noms de classe commencent toujours par une majuscule.
# Un objet est une instance d'une classe, et il possède ses propres valeurs pour ces propriétés.
class Personne: # Définition de la classe 'Personne'.
    def __init__(self, nom, age):  # Le constructeur (__init__) est appelé lors de la création d'un objet. 
        self.nom = nom  # La propriété 'nom' est initialisée avec la valeur donnée.
        self.age = age  # La propriété 'age' est initialisée avec la valeur donnée.

    def saluer(self):  # Une méthode qui fait saluer la personne.
        print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans")  # Affiche un message de salutation. Self est une référence à l'objet lui-même.

# On crée une instance de la classe 'Personne' en passant 'Jean' et 30 comme valeurs pour 'nom' et 'age'.
jean = Personne("Jean", 30)
jean.saluer()  # Affiche "Bonjour, je m'appelle Jean et j'ai 30 ans".

####################
# LES EXCEPTIONS   #
####################

# /!\ En Python, une exception est une erreur qui interrompt l'exécution du programme. Ce terme n'a rien à voir avec les exceptions en langage naturel.

# Les exceptions permettent de gérer les erreurs qui se produisent pendant l'exécution du programme.
# En cas d'erreur, l'exécution normale du programme est interrompue, mais on peut gérer cette erreur avec 'try' et 'except' pour éviter un plantage.

try: # On essaie d'exécuter le code suivant.
    resultat = 10 / 2  # Cette ligne divise 10 par 2, ce qui est correct.
    resultat = 10 / 0  # Cette ligne provoque une erreur de division par zéro.
    print(resultat)  # Cette ligne ne sera pas exécutée si une exception est levée.
except ZeroDivisionError:  # Si une erreur de type 'ZeroDivisionError' est levée, le code dans ce bloc est exécuté.
    print("Erreur : division par zéro")  # Affiche un message d'erreur expliquant le problème.

# Dans le cas où le type d'une exception est inconnue, on peut utiliser un bloc 'except' sans spécifier le type d'erreur.
# On peut également gérer plusieurs types d'exceptions en utilisant plusieurs blocs 'except'.
try:
    resultat = 10 / 0  # Cette ligne provoque une erreur de division par zéro.
except ZeroDivisionError: # Si une erreur de division par zéro est levée, le code dans ce bloc est exécuté
    print("Erreur : division par zéro") # Affiche un message d'erreur.
except: # Si une autre erreur est levée
    print("Une erreur s'est produite") # Affiche un message d'erreur générique.

# Note: Il existe de nombreux types d'exceptions en Python, comme ZeroDivisionError, ValueError, TypeError, etc.

# On peut utiliser 'finally' pour exécuter du code après le bloc 'try' / 'except', qu'une exception soit levée ou non.
try:
    resultat = 10 / 0  # Cette ligne provoque une erreur de division par zéro.
except ZeroDivisionError:
    print("Erreur : division par zéro")
finally:
    print("Le programme s'est terminé") # Affiche un message indépendamment de si une erreur s'est produite.

####################
# LES MODULES      #
####################

# Les modules sont des fichiers contenant des fonctions et des variables que l'on peut importer dans un script Python.
# Python possède une bibliothèque standard riche avec de nombreux modules pour effectuer des tâches spécifiques.

# Exemple d'importation du module 'math' pour effectuer des opérations mathématiques.
import math  # Importe le module math.

# Exemples d'utilisation des fonctions et constantes du module math :
print(math.pi)  # Affiche la valeur de pi (3.141592653589793).
print(math.sqrt(16))  # Affiche la racine carrée de 16 (4).
print(math.sin(math.pi / 2))  # Affiche le sinus de pi divisé par 2 (1.0).
print(math.cos(math.pi))  # Affiche le cosinus de pi (-1.0).
print(math.log(10))  # Affiche le logarithme naturel de 10 (2.302585092994046).
print(math.pow(2, 3))  # Affiche 2 à la puissance 3 (8).
print(math.floor(3.7))  # Affiche l'arrondi inférieur de 3.7 (3).

# Exemple d'importation du module 'random' pour générer des nombres aléatoires.
import random  # Importe le module random.

# Utilisation de la fonction randint() pour générer un nombre aléatoire entre 1 et 10.
nombre_aleatoire = random.randint(1, 10)  # Génère un nombre aléatoire entre 1 et 10.

# Exemple d'importation d'un module avec un alias.
import datetime as date  # Importe le module datetime avec l'alias 'date', ce qui permet de l'utiliser plus facilement.
# Dans ce cas, on peut utiliser 'date' au lieu de 'datetime' pour accéder aux fonctions du module.

# Utilisation du module datetime pour afficher la date et l'heure actuelles.
maintenant = date.datetime.now()  # Récupère la date et l'heure actuelles.
print(maintenant)  # Affiche la date et l'heure actuelles.

# Exemple d'importation d'une fonction spécifique d'un module.
from math import pi  # Importe la constante pi du module math.

print(pi)  # Affiche la valeur de pi (3.141592653589793).
# print(sqrt(16))  # Cette ligne provoquerait une erreur car sqrt n'est pas défini. En effet, on a importé seulement pi.

####################
# EXAMPLES         #
####################

# 1. Fonction retournant le carré d'un nombre.
def carre(nombre):
    return nombre ** 2  # La fonction retourne le carré du nombre en utilisant l'opérateur '**' pour l'exponentiation.

# 2. Afficher tous les nombres pairs de 1 à 10.
for nombre in range(1, 11):  # La fonction range génère des nombres de 1 à 10 (11 exclu).
    if nombre % 2 == 0:  # Si le nombre est divisible par 2, il est pair.
        print(nombre)  # Affiche les nombres pairs.

# 3. Fonction pour vérifier si un nombre est premier.
def est_premier(nombre):
    if nombre < 2:  # Les nombres inférieurs à 2 ne sont pas premiers.
        return False
    for diviseur in range(2, nombre):  # On teste si le nombre est divisible par un autre nombre que 1 et lui-même.
        if nombre % diviseur == 0:  # Si le nombre est divisible par 'i', il n'est pas premier.
            return False
    return True  # Si aucune division n'a eu lieu, le nombre est premier.

# 4. Calcul de la factorielle d'un nombre.
def factorielle(n):
    if n == 0:  # Par convention, la factorielle de 0 est 1.
        return 1
    resultat = 1
    for i in range(1, n + 1):  # On multiplie tous les nombres de 1 à n.
        resultat *= i
    return resultat

# 5. Classe Cercle avec calcul de l'aire.
import math  # On importe le module math pour utiliser la constante pi.

class Cercle:
    def __init__(self, rayon):  # Le constructeur prend un argument 'rayon' pour définir le rayon du cercle.
        self.rayon = rayon  # La propriété 'rayon' est initialisée avec la valeur donnée.

    def aire(self):  # Méthode pour calculer l'aire du cercle.
        return math.pi * self.rayon ** 2  # L'aire d'un cercle est donnée par la formule : pi * r^2.

# On crée un objet de la classe Cercle avec un rayon de 5.
cercle1 = Cercle(5)
print("L'aire du cercle est : ", cercle1.aire())  # Affiche l'aire du cercle avec le rayon 5.

# 6. Inverser une chaîne de caractères.
def inverser_chaine(chaine):
    return chaine[::-1]  # Utilise le "slicing" pour inverser la chaîne.

# 7. Vérifier si un mot est un palindrome.
def est_palindrome(mot):
    return mot == mot[::-1]  # Vérifie si le mot est égal à son inverse.

# Bonne chance ! 🚀
