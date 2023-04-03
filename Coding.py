# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:30:43 2023

@author: serge


"""

l = int(input())
h = int(input())

t = input().upper()
tableau = ''
longueur_t = len(t)


for i in range(h):
    tableau = tableau + input()


def num_letter(letter):
    num = ord(letter) - ord('A')
    return num


liste_numero_lettre = []

for letter in t:
    numero_lettre = num_letter(letter)
    liste_numero_lettre.append(numero_lettre)


ligne_imp = ""

for k in range(h):
    sep = ' '
    sep = tableau[1]
    if sep == '.':
        sep = '. '

    for numero_lettre in liste_numero_lettre:
        i = numero_lettre
        if i in range(26):
            indice_1 = i*l + l*27*k
            indice_2 = (i*l+l-1) + l*27*k
            ligne = str(tableau[indice_1:indice_2])
            ligne_imp = ligne_imp + ligne + ' '
        else:
            i = 26
            indice_1 = i*l + l*27*k
            indice_2 = (i*l+l-1) + l*27*k
            ligne = str(tableau[indice_1:indice_2])
            ligne_imp = ligne_imp + ligne + ' '
    ligne_imp = ligne_imp
    print(ligne_imp)
    ligne_imp = ""
