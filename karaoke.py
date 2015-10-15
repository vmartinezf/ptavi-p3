#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


def guardar_linea_atributos(dic, line):
    for elemento in dic:
        line = line + elemento    
        for dicelement in dic[elemento]:
            x = dic[elemento]
            if (x[dicelement] != ""):
                linea = '\t' + dicelement + '=' + '"' + x[dicelement]+ '"'
                line = line + linea
    return line
    

def guardar_linea(lista_etiquetas, line):
    for dic in lista_etiquetas:
        line = guardar_linea_atributos(dic, line)
        line = line + '\n'
    return line
    

def imprimir(lista_etiquetas):
    line = ""
    linea = guardar_linea(lista_etiquetas, line)
    print (linea)
     

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    try:
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
    except IOError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    imprimir(cHandler.lista_etiquetas)
