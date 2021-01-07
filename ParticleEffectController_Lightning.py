from Lightning import *
import random
randomChoiceArr = [-1,1]
directionChance = [0,1,2,3,4]

class ParticleEffectController_Lightning():
    def __init__(self,xPos,yPos,diameter,lifeDuration):
        self.x = xPos
        self.y = yPos
        self.diameter = diameter
        self.life = lifeDuration
        self.xChange = 1 * random.choice(randomChoiceArr)
        self.yChange = 2
        self.lightningArray = []
        self.timer = 0
        self.state = True
        self.lightningArray.append(Lightning(self.x,self.y,self.diameter))
        self.placementIndexX = 0
        self.placementIndexY = 0     
        
    def display(self):
        for particle in self.lightningArray:
            particle.display()
            
    def spawnLightning(self):
        if self.state == True:
            self.lightningArray.append(Lightning(self.x + self.xChange * self.placementIndexX,self.y + self.yChange * self.placementIndexY, self.diameter))
    def randomX(self):
        if random.choice(directionChance) == 4:
            self.placementIndexX *= random.choice(randomChoiceArr)
    def updateTimer(self):
        self.timer += 1
        self.placementIndexX += 10
        self.placementIndexY += 10        
    def checkYLocal(self):
        checkY = self.y + self.yChange * self.placementIndexY
        if checkY >= 960:
            self.state = False
        
    def purgeLightning(self):
        if self.state == False:
            self.placementIndex = 0
            self.lightningArray = []
        
        
        
        
