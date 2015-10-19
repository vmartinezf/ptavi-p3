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
            for elemento in dic:
                line = line + elemento
                for dicele in dic[elemento]:
                    x = dic[elemento]
                    if (x[dicele] != ""):
                        linea = '\t' + dicele + '=' + '"' + x[dicele] + '"'
                        line = line + linea
            line = line + '\n'
        print (line)

    def to_json(self, fichero, name=""):
        lista_etiq_json = json.dumps(self.lista_etiq)
        if (name == ""):
            name = fichero.split('.')[0] + '.json'
        with open(name, 'w') as fichero_json:
            json.dump(lista_etiq_json, fichero_json, sort_keys=True, indent=4)

    def do_local(self):
        for dic in self.lista_etiq:
            for elemento in dic:
                for dicele in dic[elemento]:
                    x = dic[elemento]
                    if (x[dicele] != ""):
                        if (dicele == "src") and (x[dicele] != "cancion.ogg"):
                            URL = x[dicele]
                            filename = URL[URL.rfind("/") + 1:]
                            data = urlretrieve(URL, filename)
                            urlcleanup()
                            x[dicele] = "http://" + data[0]


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
