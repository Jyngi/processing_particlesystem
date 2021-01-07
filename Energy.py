EXPLOSION_RADIUS = 300
class Energy(object):
    def __init__(self,xPos,yPos):
        self.x = random(xPos - EXPLOSION_RADIUS, xPos + EXPLOSION_RADIUS)
        self.y = random(yPos - EXPLOSION_RADIUS, yPos + EXPLOSION_RADIUS)
        self.x2 = xPos
        self.y2 = yPos
        if self.x >= xPos - 10 and self.x <= xPos + 10:
            self.x = random(xPos - EXPLOSION_RADIUS, xPos + EXPLOSION_RADIUS)
        if self.y >= xPos - 10 and self.y <= yPos + 10:
            self.y = random(yPos - EXPLOSION_RADIUS, yPos + EXPLOSION_RADIUS)
        self.angVel = (yPos - self.y) / (xPos - self.x)    
        self.checkY = False
        self.checkX = False  
        self.checkedXY = False  
    def display(self):
        fill(0)
        ellipseMode(CENTER)
        circle(self.x, self.y, 20)
    def moveCenter(self):
        if self.x >= self.x2 and self.y >= self.y2:
            self.x += -1
            self.y += self.angVel * -1
        if self.x <= self.x2 and self.y <= self.y2:
            self.x += 1
            self.y += self.angVel
        if self.x <= self.x2 and self.y >= self.y2:
            self.x += 1
            self.y += self.angVel
        if self.x >= self.x2 and self.y <= self.y2:
            self.x += -1
            self.y += -1 * self.angVel
    
    def checkXYPop(self, particleArray):
        if self.x + 10 <= self.x2 + 30 and self.x - 10 >= self.x2 - 30:
            self.checkX = True
        else:
            self.checkX = False
        if self.y + 10 <= self.y2 + 30 and self.y - 10 >= self.y2 - 30:
            self.checkY = True
        else:
            self.checkY = False
        if self.checkX and self.checkY:
            self.checkedXY = True
        else:
            self.checkedXY = False
        return filter(lambda particle: particle.checkedXY == False, particleArray)

   
        
