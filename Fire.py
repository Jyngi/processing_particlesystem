import random
directionList = [1, -1]

class Fire(object):
    def __init__(self,xPos,yPos,diameterParticle,colorParticle):
        self.x = xPos
        self.y = yPos
        self.diameter = diameterParticle
        self.decayRate = random.uniform(0.6,0.99)
        self.timer = 0
        self.state = random.choice(directionList)
        self.ownColor = colorParticle
        
    def display(self):
        pushStyle()
        fill(self.ownColor)
        noStroke()
        circle(self.x,self.y,self.diameter)
        popStyle()
    def moveY(self):
        self.y += -2 
        
    def moveX(self):
        self.timer += 1
        if self.timer >= 0:
            for i in range(int(random.randrange(4,9))):
                self.x += 0.2 * self.state
            self.state = random.choice(directionList)
        
        
    def changeSize(self):
        self.diameter *= self.decayRate
        
    def popParticles(self, particleOBJArray):
        tempArray = []
        tempArray = filter(lambda part: part.diameter > 2,particleOBJArray)
        return tempArray
