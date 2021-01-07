import random
directionList = [1, -1]

class Smoke(object):
    def __init__(self,xPos,yPos,diameterParticle):
        self.x = xPos
        self.y = yPos
        self.diameter = diameterParticle
        self.opacity = 127
        self.r = random.randrange(75,150)
        self.g = random.randrange(75,150)
        self.b = random.randrange(75,150)
        self.opacityRate = random.uniform(0.6,1.2)
        self.increaseRate = random.uniform(0.2,0.5)
        self.state = random.choice(directionList)
        self.timer = 0
        
    def display(self):
        pushStyle()
        fill(self.r,self.g,self.b,self.opacity)
        noStroke()
        circle(self.x,self.y,self.diameter)
        popStyle()
    def moveY(self):
        self.y -= 1
    def moveX(self):
        self.timer += 1
        if self.timer % 3 == 0:
            for i in range(int(random.randrange(4,9))):
                self.x += 0.2 * self.state
            self.state = random.choice(directionList)
            
    def changeSize(self):
        self.diameter += self.increaseRate
        self.opacity -= self.opacityRate
        
    def popParticles(self, particleOBJArray):
        tempArray = []
        tempArray = filter(lambda part: part.opacity > 50,particleOBJArray)
        return tempArray
