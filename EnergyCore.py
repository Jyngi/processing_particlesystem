class EnergyCore(object):
    def __init__(self, xPos,yPos, pulseSize, colorPulse):
        self.x = xPos
        self.y = yPos
        self.centerSize = 5
        self.state = 'big'
        self.pulseTimer = 0
        self.pulseSize = pulseSize
        self.pulseColor = colorPulse
    def pulse(self):
        self.centerSize += sin((self.pulseTimer * 0.1)) * self.pulseSize
        self.pulseTimer += 0.5
    def display(self):
        noStroke()
        for i in range(len(self.pulseColor)):
            fill(self.pulseColor[0], self.pulseColor[1], self.pulseColor[2], self.pulseColor[3])
        circle(self.x, self.y, self.centerSize)
