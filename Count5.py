Text = "Tfmcxc dcd lgaqnbdccqbec, nbhc rnlk bvaiblhaé yk sceegga cxzrv, garac bdrawmhmrzwc o ay rfaelbvfcefhx q'yeckrv hrg. Sblkb alcdczvd ewv adaq klckb jlraoeccbé ewbc wc ccoxrqe ck ynuotcé."
TextNew = "Toutes mes felicitations, vous avez dechiffré le dernier texte, cette introduction a la cryptographie s'acheve ici. Sinon alcdczvd ewv adaq klckb jlraoeccbé ewbc wc ccoxrqe ck ynuotcé."
ClezVegner = "Trsjtk ryl gcpiltkcjinrk, snnk rshl yrybtgcjé ng pynrycj jtcyr, ewyhy tqyjijnkyrip o py pocpsnpocpyzt y'ycvgwr zpy."

Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#         1    2    3    4     5   6     7   8    9    10   11   12   13   14   15   16   17   18   19   20   21   22   23   24  25    26
#  17 + 6 + 17 = 23 %25 =23 18

def LastLettre(Alpha, Text, TextNew):
    """Donne le changement de chaque lettre"""
    res = []
    for n in range(len(Text)):
        if Text[n] != TextNew[n] and ([Text[n], TextNew[n]] not in res):
            res.append([Text[n], TextNew[n]])
            print(Text[n], " => ", TextNew[n])

#LastLettre(Alpha, Text, TextNew)

def ChifrementDeVegnere(Alpha, Text, clez):
    """crypte en fonction d'une clé de Vegnere"""
    res = []
    for i in range(len(clez)):
        if Text[i] in Alpha:
            C = Alpha.index(Text[i])
            A = Alpha.index(clez[i])
            B = (C + A)
            res.append(B)
        else:
            res.append(Text[i])
    print(res)
    for i in res:
        if type(i) == int: 
            if i < 0:
                i += 26
            elif i >= 26:
                i -= 26
            print(Alpha[i], end="")
        else:
            print(i, end="")


ChifrementDeVegnere(Alpha, Text, TextNew)