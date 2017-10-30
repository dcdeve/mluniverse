# -*- coding: utf-8 -*-
from peewee import *
import project.config.vars as gvars
import os

db = SqliteDatabase(os.path.join(os.path.dirname(os.path.realpath(__file__)) + '/../database','weather.db'))

class Pronostic(Model):
    day = IntegerField()
    weather = TextField()
    perimeter = TextField()

    class Meta:
        database = db
        db_table = 'pronostic'
        indexes = ()

class Information(Model):
    name = CharField()
    value = TextField()

    class Meta:
        database = db
        db_table = 'information'

def getWeatherDay(day):
    try:
        result = Pronostic.get(Pronostic.day == day)
    except Pronostic.DoesNotExist:
        result = None
    return result

def initdb():
    if Pronostic.table_exists():
        Pronostic.drop_table(Pronostic)
    if Information.table_exists():
        Information.drop_table(Information)
    db.create_tables([Pronostic, Information], safe=True)
