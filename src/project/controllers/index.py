# -*- coding: utf-8 -*-
from project import api
from flask import request
from flask_restful import Resource
import json
from project.controllers.generator import *
from project.controllers.weather import *
from project.controllers.sumary import *
import project.config.vars as gvars


class GeneratorRest(Resource):
    def get(self):
        generatorObj = Generator(request.args)
        generatorObj.validateArgs()
        if generatorObj.containError() is True:
            return {'error':True, 'errorList':generatorObj.errorList}
        generatorObj.main()
        if generatorObj.containError() is True:
            return {'error':True, 'errorList':generatorObj.errorList}
        return generatorObj.totalized

class WheatherRest(Resource):
    def get(self):
        weatherObj = Weather(request.args)
        weatherObj.validateArgs()
        if weatherObj.containError() is True:
            return {'error':True, 'errorList':weatherObj.errorList}
        weatherObj.main()
        if weatherObj.containError() is True:
            return {'error':True, 'errorList':weatherObj.errorList}
        return weatherObj.result

class IndexRest(Resource):
    def get(self):
        return resumen()

api.add_resource(IndexRest, '/')
api.add_resource(GeneratorRest, '/generar')
api.add_resource(WheatherRest, '/clima')
