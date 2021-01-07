import random
from Rain import *

class ParticleEffectController_Rain():
    def __init__(self,xPos,yPos,lifeDuration):
        self.x = xPos
        self.y = yPos
        self.timer = 0
        self.rainArray = []
        self.rainArray.append(Rain(960,960))

    def display(self):
        for rainParticle in self.rainArray:
            rainParticle.display()
            
    def update(self):
        for rainParticle in self.rainArray:
            rainParticle.trail()
            rainParticle.moveYRain()
            self.rainArray =  rainParticle.popRain(self.rainArray)
    def updateTimer(self):
        self.timer += 1
    def spawnRain(self):
        if self.timer % 10 == 0:
            self.rainArray.append(Rain(960,960))
            
        
        
