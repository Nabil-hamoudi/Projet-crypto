
Text = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
########################
# Texte décrypter
TextNew = "le prochain fichier est code par un mot de passe de taille inconnue et contient l'indice. les lettres du mot de passe permettent de decaler les lettres du message original modulo 26. seules les lettres de a a z sont chiffrees."
########################
# Alphabet + ordre de frequence des lettres dans l'ordre
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

AlphaB = ["e", "a", "i", "s", "n", "r", "t", "o", "l", "u", "d", "c", "m", "p", "e", "g", "b", "v", "h", "f", "q", "y", "x", "j", "e", "a", "k", "w", "z"]
########################
# Cette fonction ma permis de rapidement testé avec un decalage simple

def DecodageCesar(cle, Text):
    """decode un texte en fonction d'une cle"""
    global Alpha
    for i in Text:
        if i not in Alpha:
            print(i, end="")
        else:
            A = cle + (Alpha.index(i))
            while A >= len(Alpha) or A < 0:
                if A < 0:
                    A += len(Alpha)
                else:
                    A -= len(Alpha)
            print(Alpha[A], end="")

#A = 8
#DecodageCesar(A, Text)

########################
# Ce code décode un texte par substitution alphabetique juste avec les frequence des lettres

def remplacementlettre(Text):
    """decode un texte par substitution alphabetique"""
    global Alpha, AlphaB
    res = [[0, 0]]
    count = 0
    for i in Alpha:
        Nb = Text.count(i)
        for p in range(count):
            if Nb > res[p][0]:
                res.insert(p, [Nb, i])
                Nb = 0
        res.append([Nb, i])
        count += 1
    res.remove([0, 0])
    reso = []
    Numb = []
    for p, i in enumerate(res[:(len(AlphaB))]):
        M = Alpha.index(i[1]) - Alpha.index(AlphaB[p])
        print(AlphaB[p] + "=>" + str(i[1]) + " Apparition : " + str(i[0]) + " Difference alphabétique: " + str(M))

#remplacementlettre(Text)

########################
# me permet de modifier le texte lettre par lettre

def SwitchLettre(Text, TextNew, lettreOld, lettreNew):
    """Modifie une lettre"""
    for i in range(len(TextNew)):
        if Text[i] == TextNew[i] and TextNew[i] == lettreOld:
            print(lettreNew, end="")
        else:
            print(TextNew[i], end="")

SwitchLettre(Text, TextNew, "m", "g")

#########################
# me permet de voir les lettres utiliser et de recuperer la clé

def LastLettre(Alpha, Text, TextNew):
    """Donne le changement de chaque lettre"""
    print("")
    res = []
    for n in range(len(Text)):
        if Text[n] != TextNew[n] and ([Text[n], TextNew[n]] not in res):
            res.append([Text[n], TextNew[n]])
            print(Text[n], " <= ", TextNew[n])

# LastLettre(Alpha, Text, TextNew)

def alphabet(Alpha, Text):
    """Donne les lettres unutiliser"""
    print("")
    res = []
    for i in Alpha:
        if i not in Text:
            print(i, end=", ")


alphabet(Alpha, TextNew)

#############################################################################
# L'alphabet de substitution est:
#
# a <= z (ici jai trouver que cetait z ayant fait le texte 3, il est impossible sinon de trouver avec certitude)
# b <= INUTILISER
# c <= d
# d <= n
# e <= INUTILISER
# f <= m 
# g <= l
# h <= INUTULISER
# i <= s
# j <= INUTILISER
# k <= i
# l <= h
# m <= g
# n <= a
# o <= r
# p <= INUTILISER
# q <= p
# r <= INUTILISER
# s <= o
# t <= INUTILISER
# u <= t
# v <= c
# w <= f
# x <= e
# y <= u
# z <= INUTILISER
#
# ici nous ne pouvons placer les lettres b, j, k, q, v, w, x, y car elle ne sont pas utiliser dans le texte decrypter
#############################################################################
# Ici pour decoder le texte jai regarder les lettres qui revenait le plus souvent et
# j'ai changer les lettres une par une afin de décoder le texte et avoir l'alphabet de substitution
#
