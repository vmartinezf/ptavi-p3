#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
from urllib.request import urlretrieve, urlcleanup


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        """
        Parseará el fichero y obtendrá etiquetas
        """
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.lista_etiq = cHandler.get_tags()

    def __str__(self):
        line = ""
        for dic in self.lista_etiq:
            llave = list(dic.keys())[0]
            line = line + llave
            for elemento in dic[llave]:
                value = dic[llave][elemento]
                if value:
                    value = dic[llave][elemento]
                    linea = '\t' + elemento + '=' + '"' + value + '"'
                    line = line + linea
            line = line + '\n'
        print (line)

    def to_json(self, fichero, name=""):
        lista_etiq_json = json.dumps(self.lista_etiq)
        if not name:
            name = fichero.split('.')[0] + '.json'
        with open(name, 'w') as fichero_json:
            json.dump(lista_etiq_json, fichero_json, sort_keys=True, indent=4)

    def do_local(self):
        for dic in self.lista_etiq:
            llave = list(dic.keys())[0]
            for elemento in dic[llave]:
                value = dic[llave][elemento]
                if value:
                    if (elemento == "src") and (value != "cancion.ogg"):
                        URL = value
                        filename = URL[URL.rfind("/") + 1:]
                        data = urlretrieve(URL, filename)
                        urlcleanup()
                        dic[llave][elemento] = data[0]


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    try:
        obj_karaokelocal = KaraokeLocal(fichero)
    except IOError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    obj_karaokelocal.__str__()
    obj_karaokelocal.to_json(fichero)
    obj_karaokelocal.do_local()
    obj_karaokelocal.to_json(fichero, 'local.json')
    obj_karaokelocal.__str__()
