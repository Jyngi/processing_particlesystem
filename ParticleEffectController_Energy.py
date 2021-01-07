from Energy import *
from EnergyCore import *

class ParticleEffectController_Energy():
    def __init__(self,xPos,yPos,lifeDuration):
        self.x = xPos
        self.y = yPos
        self.lifeSpan = lifeDuration
        self.energyCoreArray = []
        self.energyArray = []
        self.energyCoreArray.append(EnergyCore(self.x,self.y,1,[0,0,255,255]))
        self.energyCoreArray.append(EnergyCore(self.x,self.y,0.5,[255,255,255,255]))
        self.energyArray.append(Energy(self.x,self.y))
        self.timer = 0
        self.state = True
        
    def updateTimer(self):
        self.timer += 1
    def update(self):
        for energyPart in self.energyArray:
            energyPart.moveCenter()
            self.energyArray = energyPart.checkXYPop(self.energyArray)
        for core in self.energyCoreArray:
            core.pulse()
            if len(self.energyArray) <= 2 and self.state == False:
                self.energyCoreArray = []
                self.energyArray = []
    def display(self):
        for energyPart in self.energyArray:
            energyPart.display()
        for core in self.energyCoreArray:
            core.display()
    def spawnParticles(self):
        if self.timer <= self.lifeSpan and self.state == True:
            if self.timer % 10 == 0:
                self.energyArray.append(Energy(self.x,self.y))
        else:
            self.state = False
