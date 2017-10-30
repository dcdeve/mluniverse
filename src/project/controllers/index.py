# -*- coding: utf-8 -*-
from project import api
from flask import request

from flask_restful import Resource, reqparse, abort
import json
from project.controllers.generator import *
from project.controllers.weather import *
from project.controllers.sumary import *
import project.config.vars as gvars


class Generate(Resource):
    def get(self):
        generatorObj = Generator(request.args)
        generatorObj.validateArgs()
        if generatorObj.containError() is True:
            return {'error':True, 'errorList':generatorObj.errorList}
        generatorObj.tryGenerate()
        if generatorObj.containError() is True:
            return {'error':True, 'errorList':generatorObj.errorList}
        return generatorObj.totalized

class Wheather(Resource):
    def get(self):
        validateArguments = weatherValidation(request.args)
        if validateArguments['error'] is True:
            return validateArguments
        else:
            return weatherByDay(request.args)

class Index(Resource):
    def get(self):
        return resumen()

api.add_resource(Index, '/')
api.add_resource(Generate, '/generar')
api.add_resource(Wheather, '/clima')
