# -*- coding: utf-8 -*-

import json

import project.config.vars as gvars
from project.models.Weather import *

class Summary:

    def __init__(self):
        self.errorList = []

    def getResult(self):
        if self.containError() is True:
            return {'error':True, 'errorList':self.errorList}
        return self.result

    def containError(self):
        if len(self.errorList) > 0:
            return True
        return False

    def getSummary(self):
        try:
            self.result = json.loads(Information.get(Information.name == 'resumen').value)
        except Information.DoesNotExist:
            self.errorList.append('La base de datos no ha sido generada.')

    def main(self):
        self.getSummary()
