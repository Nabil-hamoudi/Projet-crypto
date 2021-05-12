Text = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
TextDec = "bravo a l'aide de l'indice vous avez reussi a casser ce code et a finir ce devoir. le dernier texte est pour les braves, regardez vous dans un miroir, en etes vous un ?"
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


#########################
# me donne l'emplacement de chaque lettre dans le but de trouver un pattern de decalage et donc le mot de passe
def emplacementlettre(Text, Alpha):
    """Donne l'emplacement de chaque lettre du texte"""
    for i in Text:
        if i in Alpha:
            print(i, " = ", Alpha.index(i)+ 1)


# emplacementlettre(Text, Alpha)

#########################
# decale une lettre par rapport a un emplacement et un nombre defini

def decalagelettre(Text, Alpha, Num, Decale):
    """Decale une lettre du texte par raport a son emplacement dans l'alphabet"""
    if Text[Num] not in Alpha:
        print(Text[Num], end="")
    else:
        res = Alpha.index(Text[Num])
        res = (res - Decale)%26
        print(Alpha[res], end="")

Code = ["c", "l",  "e", "z"]

Codei = []

for i in Code:
    Codei.append(Alpha.index(i))


for i, p in enumerate(Text):
    decalagelettre(Text, Alpha, i, Codei[i%len(Codei)])

###########################
# Ici pour trouver le texte jai chercher un mot (ici jai chercher "l'indice")
# ce qui me permettai de trouver le mot de passe assez facilement
# jai eu quelque difficulter car il fallait compter les espaces et caractéres
# spéciaux.
# Ici le code est clez
