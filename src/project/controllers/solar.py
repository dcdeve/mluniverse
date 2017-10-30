# -*- coding: utf-8 -*-

import project.config.vars as gvars
from project.controllers.planet import Planet

class SolarSystem:

    def __init__(self):
        self.ferengi = Planet('ferengi', 500, 1)
        self.betasoide = Planet('betasoide', 2000, 3)
        self.vulcano = Planet('vulcano', 1000, 5, False)

    def listPlanets(self):

        return [self.ferengi, self.betasoide, self.vulcano]

    def getPlanetByName(self, name):

        for planet in self.listPlanets():
            if planet.name == name:
                return planet

        return None

    def listPositions(self, day):
        return [p.Position(day) for p in self.listPlanets()]
