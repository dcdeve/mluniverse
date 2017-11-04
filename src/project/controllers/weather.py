# -*- coding: utf-8 -*-

import json

import project.config.vars as gvars
from project.models.Weather import *

class Weather:

    def __init__(self, getArgs):
        self.getArgs = getArgs
        self.errorList = []
        self.defaultData = {}

    def getResult(self):
        if self.containError() is True:
            return {'error':True, 'errorList':self.errorList}
        return self.result

    def containError(self):
        if len(self.errorList) > 0:
            return True
        return False

    def validateArgs(self):
        # day validation
        if 'dia' in self.getArgs:
            if self.getArgs['dia'].isdigit():
                if int(self.getArgs['dia']) > gvars.MAX_DB_INT:
                    self.errorList.append('El argumento <dia> esta fuera de rango.')
            else:
                self.errorList.append('Error en tipo de dato <dia>.')
        else:
            self.errorList.append('Debe indicar al menos un dia.')

    def getToVars(self):
        self.day = self.getArgs['dia']

    def main(self):
        self.getToVars()
        getDay = getWeatherDay(self.day)
        if getDay is not None:
            self.result = {
                'dia': getDay.day,
                'clima': getDay.weather
                }
        else:
            self.errorList.append('El dia seleccionado no ha sido generado.')
