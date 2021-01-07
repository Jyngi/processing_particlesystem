from Fire import *
import random

class ParticleEffectController():
    def __init__(self,orgMouseX,orgMouseY,lifeDuration):
        self.x = orgMouseX
        self.y = orgMouseY
        self.life = lifeDuration
        self.fireParticleArray = []
        self.adjunctFireArrayOrange = []
        self.adjunctFireArrayYellow = []
        self.timer = 0
        self.state = True
        self.fireParticleArray.append(Fire(self.x,self.y,30,color(255,0,0,127)))
        self.adjunctFireArrayOrange.append(Fire(self.x,self.y,15,color(252,127,3,127)))
        self.adjunctFireArrayYellow.append(Fire(self.x,self.y,5,color(252,236,3,127)))
        
    def update(self):
        for particle in self.fireParticleArray:
            particle.moveY()
            particle.moveX()
            particle.changeSize()
            self.fireParticleArray = particle.popParticles(self.fireParticleArray)
        for particleOrange in self.adjunctFireArrayOrange:
            particleOrange.moveY()
            particleOrange.moveX()
            particleOrange.changeSize()
            self.adjunctFireArrayOrange = particleOrange.popParticles(self.adjunctFireArrayOrange)
        for particleYellow in self.adjunctFireArrayYellow:
            particleYellow.moveY()
            particleYellow.moveX()
            particleYellow.changeSize()
            self.adjunctFireArrayYellow = particleYellow.popParticles(self.adjunctFireArrayYellow)
            
    def display(self):
        for particle in self.fireParticleArray:
            particle.display()
        for particleOrange in self.adjunctFireArrayOrange:
            particleOrange.display()
        for particleYellow in self.adjunctFireArrayYellow:
            particleYellow.display()
            
    def updateTimer(self):
        self.timer += 1
    def lifeSpan(self):
        if self.timer <= self.life and self.state == True:
            self.fireParticleArray.append(Fire(self.x + random.randrange(-5,5),self.y,30,color(255,0,0,127)))
            self.adjunctFireArrayOrange.append(Fire(self.x + random.randrange(-5,5),self.y + 5,20,color(252,127,3,127)))
            self.adjunctFireArrayYellow.append(Fire(self.x + random.randrange(-5,5),self.y + 15,10,color(252,236,3,127)))
        else:
            self.state = False
        
            
        
