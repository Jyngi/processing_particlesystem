
class Lightning(object):
    def __init__(self,xPos,yPos,outerDiameter):
        self.x = xPos
        self.y = yPos
        self.outerColor = color(0,0,255,55)
        self.innerColor = color(64,242,255,110)
        self.coreColor = color(255,255,255,165)
        self.outerDiameter = outerDiameter
        self.innerDiameter = self.outerDiameter - 10
        self.coreDiameter = self.outerDiameter - 20
        
    def display(self):
        pushStyle()
        noStroke()
        fill(self.outerColor)
        circle(self.x,self.y,self.outerDiameter)
        popStyle()
        
        pushStyle()
        noStroke()
        fill(self.innerColor)
        circle(self.x,self.y,self.innerDiameter)
        popStyle()
        
        pushStyle()
        noStroke()
        fill(self.coreColor)
        circle(self.x,self.y,self.coreDiameter)
        popStyle()
        
        
