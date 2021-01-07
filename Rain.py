import random

class Rain(object):
    def __init__(self, maxX, maxY):
        self.x = random.uniform(0,maxX)
        self.y = -50
        self.slope = 0.5
        self.colorIndexBody = color(79,103,255)
        self.colorIndexHead = color(184,240,255)
        self.diameterRain = 5
        self.rainTrail = []
        self.opacity = 127
        self.particleSpeed = random.randrange(3,12)
        
    def display(self):
        noStroke()
        fill(self.colorIndexHead)
        circle(self.x,self.y,self.diameterRain)
    
    def moveYRain(self):
        self.y += self.particleSpeed
        
    def popRain(self, rainOBJArray):
        return filter(lambda rain: rain.y <= 1060, rainOBJArray) 
    def trail(self):
        self.rainTrail.append([self.x,self.y,5])
        pushStyle()
        for trailParticle in self.rainTrail:
            trailParticle[2] -= 0.5
            if trailParticle[2] <= 0.1:
                self.rainTrail.pop(0) 
        for x,y,s in self.rainTrail:
            fill(self.colorIndexBody)
            circle(x,y,s)
        popStyle()
        
