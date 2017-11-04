# -*- coding: utf-8 -*-
from project import api
from flask import request
from flask_restful import Resource
import json
from project.controllers.generator import *
from project.controllers.weather import *
from project.controllers.summary import *
import project.config.vars as gvars


class GeneratorRest(Resource):
    def get(self):
        generatorObj = Generator(request.args)
        generatorObj.validateArgs()
        if generatorObj.containError() is False:
            generatorObj.main()
        return generatorObj.getResult()

class WheatherRest(Resource):
    def get(self):
        weatherObj = Weather(request.args)
        weatherObj.validateArgs()
        if weatherObj.containError() is False:
            weatherObj.main()
        return weatherObj.getResult()

class SummaryRest(Resource):
    def get(self):
        summaryObj = Summary()
        summaryObj.main()
        return summaryObj.getResult()

api.add_resource(SummaryRest, '/')
api.add_resource(GeneratorRest, '/generar')
api.add_resource(WheatherRest, '/clima')
