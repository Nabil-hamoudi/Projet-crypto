TextPart1 = [
            "jeqeqecvnf suozvb jfk muj",
            "dfjr fmy rvuqsk ve",
            "itajtd mifwz nnrt",
            "imtrvp zuh srzmzbqz tepr zn",
            "tmsnirt imtrvp nec hw",
            "dzpqj tjf pdecpr zl jr",
            "ptejnt ekpb iu b",
            "iiuyu iy ijz surg rjs ttsn",
            "votp ac hw rzpuen jozw",
            "rvwdvx jbo nirscyjv fi"
            ]
TextPart2 = [
             "svmkyw ve iaflss yie te",
             "teffvv'u riznxjzvv jfk",
             "nelrhtjrk dh sivdvjvve",
             "yi cvb à jffrds tdp",
             "rvwdv sebr onvnqsy zvp",
             "zuhjwiM le wmifo wiezib nec",
             "triot qmjvr'c onrwz",
             "memfqg srq wdaietsq vk"
            ]

Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

##############################################
# Ce code me permet de mettre le texte en inversion horizontal et vertical

for i in range(len(TextPart1)):
    TextPart1[i] = list(TextPart1[i])
    TextPart1[i].reverse()
for i in range(len(TextPart2)):
    TextPart2[i] = list(TextPart2[i])
    TextPart2[i].reverse()

TextPart1.reverse()
TextPart2.reverse()

#######################
# Ce code me permet de decoder le texte en fonction d'une cle

def decalagelettre(Text, Alpha, Num, Decale):
    """Decale une lettre du texte par raport a son emplacement dans l'alphabet"""
    if Text[Num] not in Alpha:
        print(Text[Num], end="")
    else:
        res = Alpha.index(Text[Num])
        res = (res - Decale)%26
        print(Alpha[res], end="")

Code = ["b", "r", "a", "v", "e", "z"]

Codei = []

for i in Code:
    Codei.append(Alpha.index(i))

Index = 0

for ligne in TextPart2:
    for i, p in enumerate(ligne):
        decalagelettre(ligne, Alpha, i, Codei[Index%len(Codei)])
        Index += 1
    Index += 1
    print("")

Index += 1
print(" ")

for ligne in TextPart1:
    for i, p in enumerate(ligne):
        decalagelettre(ligne, Alpha, i, Codei[Index%len(Codei)])
        Index += 1
    Index += 1
    print("")


########################################################
# Texte décoder:
#
# je voudrais pas crever
# avant d'avoir connu
# les chiens noirs du Mexique
# qui dorment sans rever
# les singes à cul nu
# devoreurs de tropiques
# les araignees d'argent
# au nid truffe de bulles
# 
# je voudrais pas crever
# sans savoir si la lune
# sous son faux air de thune
# a un cote pointu
# si le soleil est froid
# si les quatre saisons
# ne sont vraiment que quatre
# sans avoir essaye
# de porter une robe
# sur les grands boulevards
#
# Le mot de passe est: bravez
########################################
# Pour décoder ce texte jai d'abord chercher un mot precis (ici est)
# une fois avoir trouver une suite de 3 lettres logique pour le code
# (jai trouver bra) il fut assez simple de trouver le reste du code
# j'ai eu 2 3 soucis par le fait que les retours a la ligne sont compter 
# et que il a une inversion vertical ce qui n'est pas normalement le cas sur
# un mirroir
#########################################
