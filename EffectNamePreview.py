class EffectNamePreview():
    def __init__(self,xPos,yPos):
        self.x = xPos
        self.y = yPos
        
    def update(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
    
    def display(self, particleName, modeName):
        fill(0)
        text(particleName, self.x + 10, self.y - 10)
        text(modeName, self.x + 10, self.y + 5)
