#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


from smallsmilhandler import SmallSMILHandler


if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        fich = open(fichero, 'r')
        fich.close()
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
    except IOError:
        sys.exit("Usage: python3 karaoke.py file.smil.")
