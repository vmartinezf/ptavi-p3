#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar smill
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.rootlayout = ""
        self.region = ""
        self.inRegion = 0
        self.img = ""
        self.inImg = 0
        self.audio = ""
        self.inAudio = 0
        self.textstream = ""
        self.inTextstream = 0

    def get_tags(self, name, lista_etiquetas, atributo):
        """
        Método que se llama para alamacenar las etiquetas,
        los atributos y su contenido
        """
        lista_etiquetas.append = ('')

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.rootlayout = attrs.get('width', "")  # FALTA ALGO
        elif name == 'region':
            self.inRegion = 1
        elif name == 'img':
            self.inImg = 1
        elif name == 'audio':
            self.inAudio = 1
        elif name == 'textstream':
            self.inTextstream = 1

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'region':
            self.region = ""
            self.inRegion = 0
        if name == 'img':
            self.img = ""
            self.inImg = 0
        if name == 'audio':
            self.audio = ""
            self.inImg = 0
        if name == 'textstream':
            self.textstream = ""
            self.inTextstream = 0

    def characters(self, char):
        """
        Método para tomar contenido de la etiqueta
        """
        if self.inRegion:
            self.region = self.region + char
        if self.inImg:
            self.img = self.img + char
        if self.inAudio:
            self.audio = self.audio + char
        if self.inTextstream:
            self.textstream = self.stream + char


if __name__ == "__main__":
    """
    Programa principal
    """
    lista_etiquetas = []
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
