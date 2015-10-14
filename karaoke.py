#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


def imprimir(lista_etiquetas):
    for dic in lista_etiquetas:
        for elemento in dic:
    #        print(elemento)
  #          print (dic[elemento])
            for dicelement in dic[elemento]:
 #               print (dicelement)
                x = dic[elemento]
#                print (x[dicelement])
                if (x[dicelement] != ""):
                    linea = '\t' + dicelement + '=' + '"' + x[dicelement]+ '"'
                
     


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        imprimir(cHandler.lista_etiquetas)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    except IOError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
