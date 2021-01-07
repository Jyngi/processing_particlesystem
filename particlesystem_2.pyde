import random
from ParticleSystem import *
from EffectNamePreview import *

WIDTH = 960
HEIGHT = 960
p = None
n = None
buttonArray = []
particleEffectName = ['fire','rain','energy','lightning','smoke']
particleEffectState = ['timed', 'loop']
particleEffectStateIndex = 0
particleEffectIndex = 0
# [Down, Up]
keyInputState = [False,False]


def setup():
    global n
    size(WIDTH,HEIGHT)
    frameRate(120)
    n = EffectNamePreview(0,0)

    
def draw():
    if particleEffectName[particleEffectIndex] == 'fire':
        backgroundFire()
    if particleEffectName[particleEffectIndex] == 'rain':
        backgroundRain()
    if particleEffectName[particleEffectIndex] == 'lightning':
        backgroundLightning()
    if particleEffectName[particleEffectIndex] == 'smoke':
        backgroundSmoke()
    if particleEffectName[particleEffectIndex] == 'energy':
        backgroundEnergy()
    textController()
        
    if p:
        p.update()
        p.render()
        if mousePressed:
            p.addParticleEffect(particleEffectName[particleEffectIndex], particleEffectState[particleEffectStateIndex])
    # if n:
    #     n.update(mouseX,mouseY)
    #     n.display(particleEffectName[particleEffectIndex], particleEffectState[particleEffectStateIndex])
    # Debug stuff

    
def mousePressed():
    global p
    if particleEffectName[particleEffectIndex] != 'lightning':
        p = ParticleSystem(mouseX,mouseY,random.randrange(60,80))
    else:
        p = ParticleSystem(mouseX,0,random.randrange(60,80))
    
def keyPressed():
    global particleEffectIndex, particleEffectStateIndex
    if key == 's' or key == 'S' or keyCode == DOWN:
        particleEffectIndex -= 1
        if particleEffectIndex < 0 :
            particleEffectIndex = len(particleEffectName) - 1
    if key == 'w' or key == 'W' or keyCode == UP:
        particleEffectIndex += 1
        if particleEffectIndex >= len(particleEffectName):
            particleEffectIndex = 0
    if key == '1':
        particleEffectStateIndex += 1
        if particleEffectStateIndex > len(particleEffectState) - 1:
            particleEffectStateIndex = 0
    if keyCode == SHIFT:
        p.clearAll()
        
def backgroundFire():
    background(255,207,207)
def backgroundLightning():
    background(100,100,100)
def backgroundRain():
    background(194,222,255)
def backgroundSmoke():
    background(181)
def backgroundEnergy():
    background(171,255,190)
def textController():
    pushStyle()
    textSize(100)
    textAlign(CENTER,BOTTOM)
    if particleEffectName[particleEffectIndex] != 'rain' and particleEffectName[particleEffectIndex] != 'lightning':
        fill(224,195,141)
        text(particleEffectName[particleEffectIndex].upper(),(WIDTH/2) + 5,115)
        text(particleEffectState[particleEffectStateIndex].upper(),(WIDTH/2) + 5, HEIGHT)
        fill(255,255,219)
        text(particleEffectName[particleEffectIndex].upper(),WIDTH/2, 110)
        text(particleEffectState[particleEffectStateIndex].upper(),(WIDTH/2),HEIGHT-5)
    if particleEffectName[particleEffectIndex] == 'rain':
        fill(224,195,141)
        text(particleEffectName[particleEffectIndex].upper(),(WIDTH/2) + 5,115)
        text(particleEffectState[1].upper(),(WIDTH/2) + 5, HEIGHT)
        fill(255,255,219)
        text(particleEffectName[particleEffectIndex].upper(),WIDTH/2, 110)
        text(particleEffectState[1].upper(),(WIDTH/2),HEIGHT-5)   
    if particleEffectName[particleEffectIndex] == 'lightning':
        fill(224,195,141)
        text(particleEffectName[particleEffectIndex].upper(),(WIDTH/2) + 5,115)
        text(particleEffectState[0].upper(),(WIDTH/2) + 5, HEIGHT)
        fill(255,255,219)
        text(particleEffectName[particleEffectIndex].upper(),WIDTH/2, 110)
        text(particleEffectState[0].upper(),(WIDTH/2),HEIGHT-5) 
    popStyle()
    
    
    
        

        
    
