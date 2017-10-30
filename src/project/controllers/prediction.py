# -*- coding: utf-8 -*-

import math
import numpy
import project.config.vars as gvars

class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def asTuple(self):
        """(x, y)"""
        return (self.x, self.y)

class Predict:

    def distance(self, a, b):
        return numpy.array( numpy.array( a ) - numpy.array( b ) )

    def crossProduct(self, a, b):
        return numpy.cross( numpy.array( a ), numpy.array( b ) )

    def Rain(self):
        p0 = self.p1
        p1 = self.p2
        p2 = self.p3
        p = Point(0,0)
        s = p0.y * p2.x - p0.x * p2.y + (p2.y - p0.y) * p.x + (p0.x - p2.x) * p.y
        t = p0.x * p1.y - p0.y * p1.x + (p0.y - p1.y) * p.x + (p1.x - p0.x) * p.y

        if ((s < 0) != (t < 0)):
            return False
        A = -p1.y * p2.x + p0.y * (p2.x - p1.x) + p0.x * (p1.y - p2.y) + p1.x * p2.y
        if (A < 0.0):
            s = -s
            t = -t
            A = -A
        return s > 0 and t > 0 and (s + t) <= A

    def Drought(self):
        if self.crossProduct(self.p1.asTuple(), self.p3.asTuple()) == 0 and \
        self.crossProduct(self.p1.asTuple(), self.p2.asTuple()) == 0 and \
        self.crossProduct(self.p1.asTuple(), self.p3.asTuple()) == 0:
            return True
        return False


    def Optimal(self):
        a = self.distance(self.p1.asTuple(), self.p2.asTuple())
        b = self.distance(self.p2.asTuple(), self.p3.asTuple())
        if 1 > abs(numpy.dot(a, b) / (numpy.linalg.norm(a) * numpy.linalg.norm(b))) >= (1 - gvars.OPTIMAL_TOLERANCE_ROUND) or \
            self.crossProduct(a, b) == 0:
            return True
        return False

    def getPerimeter(self):
        a1 = self.distance(self.p1.asTuple(), self.p2.asTuple())
        a2 = self.distance(self.p2.asTuple(), self.p3.asTuple())
        a3 = self.distance(self.p1.asTuple(), self.p3.asTuple())

        return numpy.linalg.norm(a1) + numpy.linalg.norm(a2) + numpy.linalg.norm(a3)

    def setPositions(self, listPositions):
        [self.p1, self.p2, self.p3] = listPositions

    def checkWeather(self):
        result = {'name':None}
        if self.Drought():
            result['name'] = gvars.DROUGHT_NAME
        elif self.Rain():
            result['name'] = gvars.RAIN_NAME
            result['perimetro'] = self.getPerimeter()
        elif self.Optimal():
            result['name'] = gvars.OPTIMAL_NAME
        return result
