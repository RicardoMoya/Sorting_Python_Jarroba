# -*- coding: utf-8 -*-
__author__ = 'RicardoMoya'


class Futbolista:

    def __init__(self, dorsal, nombre, demarcacion):
        self.dorsal = dorsal
        self.nombre = nombre
        self.demarcacion = demarcacion

    def __str__(self):
        return "%i - %s - %s" % (self.dorsal, self.nombre, self.demarcacion)
