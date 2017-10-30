# -*- coding: utf-8 -*-

import json

import project.config.vars as gvars
from project.models.Weather import *

defaultData = {}

def weatherValidation(getArguments):
    errorList = []
    # day validation
    if 'dia' in getArguments:
        if not getArguments['dia'].isdigit():
            errorList.append('Error en tipo de dato <dia>.')
    else:
        errorList.append('Debe indicar al menos un dia.')
    # Evaluating errores in validation
    if len(errorList) > 0:
        return {'error':True, 'errorList':errorList}

    return {'error':False}

def weatherByDay(getArguments):
    day = getArguments['dia']
    result = getWeatherDay(day)
    if result is not None:
        return {
            'dia': result.day,
            'clima': result.weather
            }
    return {'error':'true', 'errorList':['El dia seleccionado no ha sido generado.']}
