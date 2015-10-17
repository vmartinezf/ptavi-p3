#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve, urlcleanup


def convertir_a_local(lista_etiquetas):
    for dic in lista_etiquetas:
        for elemento in dic:
            for dicelement in dic[elemento]:
                x = dic[elemento]
                if (dicelement == "src" and x[dicelement] != "cancion.ogg"):
                    URL = x[dicelement]
                    filename = URL[URL.rfind("/") + 1:]
                    data = urlretrieve(URL, filename)
                    urlcleanup()
                    x[dicelement] = "http://" + data[0]
    return lista_etiquetas


def guardar_linea_atributos(dic, line):
    for elemento in dic:
        line = line + elemento
        for dicelement in dic[elemento]:
            x = dic[elemento]
            if (x[dicelement] != ""):
                linea = '\t' + dicelement + '=' + '"' + x[dicelement] + '"'
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


def crear_fichero_json(lista_etiquetas):
    lista_etiquetas_json = json.dumps(lista_etiquetas)
    with open('karaoke.json', 'w') as fichero_json:
        json.dump(lista_etiquetas_json, fichero_json, sort_keys=True, indent=4)
        # Muestro por pantalla el fichero json
        print (lista_etiquetas_json)


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
    cHandler.lista_etiquetas = convertir_a_local(cHandler.lista_etiquetas)
    imprimir(cHandler.lista_etiquetas)
    crear_fichero_json(cHandler.lista_etiquetas)
