# -*- coding: utf-8 -*-

import math
import numpy
from project.controllers.prediction import Point
import project.config.vars as gvars

class Planet:


    def __init__(self, name, distance, angular_speed, schedule=True):
        self.name = name
        self.distance = distance
        self.angular_speed = -angular_speed if schedule else angular_speed

    def daysForYear(self):

        return abs(int(gvars.CIRCLE_GRADES / self.angular_speed))

    def __round(self, value):
        return 0 if numpy.allclose(value, 0) else value

    def Position(self, day):
        delta = math.radians(self.angular_speed) * day
        return Point(self.distance * self.__round(math.cos(delta)), self.distance * self.__round(math.sin(delta)))
