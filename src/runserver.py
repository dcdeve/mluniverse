#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from project import app

def argPort(listArgs):
    try:
        portNum = listArgs[1]
    except IndexError:
        return 8080
    if portNum.isdigit():
        if int(portNum) > 0 and int(portNum) < 65536:
            return int(portNum)
        else:
            print('El numero de puerto debe ser mayor a 0 y menor a 65536.')
            quit()
    else:
        print('El puerto debe ser numerico.')
        quit()

if __name__ == '__main__':
    portNum = argPort(sys.argv)
    port = int(os.environ.get("PORT", portNum))
    app.run('0.0.0.0', port=port)
