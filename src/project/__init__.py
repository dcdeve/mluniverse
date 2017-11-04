# -*- coding: utf-8 -*-
__version__ = '0.3'
from flask import Flask
from flask_restful import Api
app = Flask('project')
api = Api(app)
app.config['SECRET_KEY'] = 'random'
app.debug = True
from project.controllers import *
