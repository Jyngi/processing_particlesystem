from Smoke import *
import random

class ParticleEffectController_Smoke():
    def __init__(self,xPos,yPos,duration):
        self.x = xPos
        self.y = yPos
        self.life = duration
        self.smokeArray = []
        self.timer = 0
        self.state = True
        self.smokeArray.append(Smoke(self.x,self.y,30))
        
    def update(self):
        for smokeParticle in self.smokeArray:
            smokeParticle.moveY()
            smokeParticle.moveX()
            smokeParticle.changeSize()
            self.smokeArray = smokeParticle.popParticles(self.smokeArray)
            
    def display(self):
        for smokeParticle in self.smokeArray:
            smokeParticle.display()
        
    def lifeSpan(self):
        if self.state == True and self.timer <= self.life:
            if self.timer % 4 == 0:
                self.smokeArray.append(Smoke(self.x + random.randrange(-20,20), self.y, 30))
        else:
            self.state = False
            
    def updateTimer(self):
        self.timer += 1
            
        
