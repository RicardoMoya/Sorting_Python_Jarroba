# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'

from Futbolista import Futbolista

futbolistasOb = list()
futbolistasOb.append(Futbolista(1,'Casillas','Portero'))
futbolistasOb.append(Futbolista(15,'Ramos','Lateral Derecho'))
futbolistasOb.append(Futbolista(3,'Pique','Central'))
futbolistasOb.append(Futbolista(5,'Puyol','Central'))
futbolistasOb.append(Futbolista(11,'Capdevila','Lateral Izquierdo'))
futbolistasOb.append(Futbolista(14,'Xabi Alonso','Medio Centro'))
futbolistasOb.append(Futbolista(16,'Busquets','Medio Centro'))
futbolistasOb.append(Futbolista(8,'Xavi Hernandez','Centro Campista'))
futbolistasOb.append(Futbolista(18,'Pedrito','Interior Izquierdo'))
futbolistasOb.append(Futbolista(6,'Iniesta','Interior Derecho'))
futbolistasOb.append(Futbolista(7,'Villa','Delantero'))

# Ordenamos los objetos de la Clase Futbolista por el atributo Dorsal
futbolistasOb.sort(key=lambda futbolista: futbolista.dorsal)
print "Futbolistas ordenados por el atributo Dorsal"
for i in futbolistasOb:
    print i

# Ordenamos los objetos de la Clase Futbolista por el atributo Dorsal (decreciente)
futbolistasOb.sort(key=lambda futbolista: futbolista.dorsal, reverse=True)
print "\nFutbolistas ordenados descendentemente por el atributo Dorsal"
for i in futbolistasOb:
    print i

# Ordenamos los objetos de la Clase Futbolista por el atributo Nombre (decreciente)
futbolistasOb.sort(key=lambda futbolista: futbolista.nombre, reverse=True)
print "\nFutbolistas ordenados descendentemente por el atributo Nombre"
for i in futbolistasOb:
    print i
