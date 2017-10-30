# -*- coding: utf-8 -*-

import json

import project.config.vars as gvars
from project.models.Weather import *

def getResumen():
    try:
        result = Information.get(Information.name == 'resumen')
    except Information.DoesNotExist:
        result = None
    return result

def resumen():
    result = getResumen()
    if result is not None:
        return json.loads(result.value)
    return {'error':'true', 'errorList':['La base de datos no ha sido generada.']}
