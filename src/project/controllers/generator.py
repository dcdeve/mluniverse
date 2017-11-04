# -*- coding: utf-8 -*-

import json
from project.controllers.prediction import Predict
from project.controllers.solar import SolarSystem
import project.config.vars as gvars
from project.models.Weather import *

solar = SolarSystem()
pr = Predict()

class Generator:

    def __init__(self, getArgs):
        self.getArgs = getArgs
        self.errorList = []
        self.result = {'error':False, 'total_dias': 0, 'pico_lluvia': {'dia': None, 'perimetro': 0}}
        self.defaultData = {'planeta':solar.vulcano.name, 'anios':0, 'dias':0}

    def getResult(self):
        if self.containError() is True:
            return {'error':True, 'errorList':self.errorList}
        return self.result

    def containError(self):
        if len(self.errorList) > 0:
            return True
        return False

    def validateArgs(self):
        # from_planet validation
        if 'planeta' in self.getArgs:
            if solar.getPlanetByName(self.getArgs['planeta'].lower()) is None:
                self.errorList.append('El planeta indicado no es valido.')
        # Days and Years validation
        if ('dias' in self.getArgs or 'anios' in self.getArgs):
            if 'dias' in self.getArgs:
                if not self.getArgs['dias'].isdigit():
                    self.errorList.append('El tipo de dato en el item <dias> es incorrecto.')
            if 'anios' in self.getArgs:
                if not self.getArgs['anios'].isdigit():
                    self.errorList.append('El tipo de dato en el item <anios> es incorrecto.')
        else:
            self.errorList.append('Debe indicar dias o anios a generar.')

    def getToVars(self):
        # Obtain get arguments
        #   planeta
        if 'planeta' in self.getArgs:
            self.planet = solar.getPlanetByName(self.getArgs['planeta'].lower())
        else:
            self.planet = solar.getPlanetByName(self.defaultData['planeta'])
        #   dias
        if 'dias' in self.getArgs:
            self.days = int(self.getArgs['dias'])
        else:
            self.days = int(self.defaultData['dias'])
        #   anios
        if 'anios' in self.getArgs:
            self.years = int(self.getArgs['anios'])
        else:
            self.years = int(self.defaultData['anios'])

    def main(self):
        self.getToVars()
        # Reset db
        initdb()

        self.result['total_dias'] = self.days + self.planet.daysForYear() * self.years

        total_days = Information(name='total_dias', value='%s' % (self.result['total_dias']))
        total_days.save()

        for day in range(int(total_days.value)):
            pr.setPositions(solar.listPositions(day))
            prediction = pr.checkWeather()
            self.result.setdefault(prediction['name'], 0)
            self.result[prediction['name']] += 1

            perimeter = 0.0
            if 'perimetro' in prediction:
                perimeter = prediction['perimetro']

            pronostic = Pronostic(day= day, weather='%s' % (prediction['name']), perimeter='%f' % (perimeter))
            pronostic.save()

            if 'perimetro' in prediction and \
                    prediction['perimetro'] > self.result['pico_lluvia']['perimetro']:
                self.result['pico_lluvia']['perimetro'] = prediction['perimetro']
                self.result['pico_lluvia']['dia'] = day

        max_rain = Information(name='pico_lluvia', value='%s' % (json.dumps(self.result['pico_lluvia'])))
        max_rain.save()

        summary = Information(name='resumen', value='%s' % (json.dumps(self.result)))
        summary.save()
