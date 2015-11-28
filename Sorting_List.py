# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'



# Lista de Tuplas
futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"),
                  (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

# Ordenamos la lista por numero de dorsal; es decir por la primera posición de las tuplas que hay en la lista
futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print "Imprimimos las lista ordenada por dorsal:"
print futbolistasTup

# Ordenamos la lista por dorsal pero en orden decreciente
futbolistasTup.sort(key=lambda futbolista: futbolista[0], reverse=True)
print "\nImprimimos las lista ordenada descendentemente por dorsal:"
print futbolistasTup

# Ordenamos la lista por nombre; es decir por la segunda posición de las tuplas que hay en la lista
futbolistasTup.sort(key=lambda futbolista: futbolista[1])
print "\nImprimimos las lista ordenada por el nombre del jugador:"
print futbolistasTup


# Lista de Strings
futbolistas = ["1 - Casillas", "15 - Ramos", "3 - Pique", "5 - Puyol", "11 - Capdevila", "14 - Xabi Alonso",
                  "16 - Busquets", "8 - Xavi Hernandez", "18 - Pedrito", "6 - Iniesta", "7 - Villa"]

# Ordenamos la lista por el nombre del futbolista, haciendo un split del string
futbolistas.sort(key=lambda futbolista: futbolista.split("-")[1], reverse=True)
print "\nImprimimos las lista ordenada por el nombre del jugador:"
print futbolistas
