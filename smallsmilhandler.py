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
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.imgregion = ""
        self.begin = ""
        self.dur = ""
        self.lista_etiquetas =  []

        #self.dic = {
         #   'root-layout': ['width', 'height'] }

    def startElement(self, name, attrs):
        """
        Método que se llama para alamacenar las etiquetas,
        los atributos y su contenido
        """

        #if name == 'root-layout':
         #   for item in self.dic[name]:
                # guardo en un dic..
          #      dicrootlayout = {name : self.dic[name]}
                

        if name == 'root-layout':
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('background-color', "")
            dicrootlayout = {'width': self.width, 'height': self.height, 'background-color' : self.backgroundcolor}
            rootlayout = {'root-layout' : dicrootlayout}
            self.lista_etiquetas.append(rootlayout) 
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            dicregion = {'id': self.id, 'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right}
            region = {'region': dicregion}
            self.lista_etiquetas.append(region) 
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            dicimg = {'src': self.src, 'region': self.region, 'begin': self.begin, 'dur': self.dur}
            self.lista_etiquetas.append(dicimg)       
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            dicaudio = {'src': self.src, 'begin': self.begin, 'dur': self.dur}
            self.lista_etiquetas.append(dicaudio)
            self.inAudio = 1
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            dictextstream = {'src': self.src, 'region': self.region}
            self.lista_etiquetas.append(dictextstream)

    def get_tags (self):
        """
        Método que devuelve las etiquetas,
        los atributos y su contenido
        """
        return self.lista_etiquetas

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print (cHandler.get_tags())
