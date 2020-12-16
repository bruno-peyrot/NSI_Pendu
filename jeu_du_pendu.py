import random

# Importation du dictionnaire
dico = []
NomFichier = 'dico.txt'
fichier = open(NomFichier, 'r')
for ligne in fichier:
    dico.append(ligne[:len(ligne) - 1])
fichier.close()

# Sélection du mot mystère et création du "mot caché"
mystere = dico[random.randint(0, len(dico) - 1)]
mystere = mystere.upper()
mystere2 = mystere[1:len(mystere)-1]
mot = mystere[0] + (len(mystere) - 2) * '*' + (mystere[len(mystere) - 1])

# Définition des variables
bonnes = []
mauvaises = []
vies = 10
restantes = len(mystere) - 2

# Boucle principale
while (vies != 0):
    print(' ')
    print(mot)
    print('Il vous reste ', vies, ' vies')
    print('Il reste ', restantes, ' lettres à trouver !')
    print('Mauvaises lettres : ', end = ' ')
    for i in range(len(mauvaises)):
        print(mauvaises[i], end = ' ')
    print(' ')
    lettre = input('Entrez une lettre : ')
    lettre = lettre.upper()
    if ((lettre in mauvaises) or (lettre in bonnes)):
        print(' ')
        print('Vous avez déjà proposé cette lettre !')
    else:
        for i in range(1, len(mystere) - 1):
            if (mystere[i] == lettre):
                restantes = restantes - 1
                mot = mot[:i] + mystere[i] + mot[i+1:]
        if (not(lettre in mystere2)):
            vies = vies - 1
            mauvaises.append(lettre)
        else:
            bonnes.append(lettre)
        if (restantes == 0):
            break
if (restantes == 0):
    print(' ')
    print('Bravo ! Vous avez trouvé le mot ', mystere)
    print('Il vous restait ', vies, ' vies !')
else:
    print(' ')
    print('Perdu ! Il vous restait ', restantes, ' lettres à trouver.')
    print('Le mot mystère était : ', mystere)
