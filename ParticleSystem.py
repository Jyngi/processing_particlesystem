from ParticleEffectController import *
from ParticleEffectController_Smoke import *
from ParticleEffectController_Lightning import *
from ParticleEffectController_Rain import *
from ParticleEffectController_Energy import *
particleEffectArrayLightning = []
particleEffectArrayFire = []
particleEffectArraySmoke = []
particleEffectArrayRain = []
particleEffectArrayEnergy = []

class ParticleSystem:
    def __init__(self,positionX,positionY,lifeSpan):
        self.x = positionX
        self.y = positionY
        self.life = lifeSpan

        
    def update(self):
        for particleEffect in particleEffectArrayFire:
            particleEffect.update()
            particleEffect.updateTimer()
            particleEffect.lifeSpan()
        for particleEffectSmoke in particleEffectArraySmoke:
            particleEffectSmoke.update()
            particleEffectSmoke.updateTimer()
            particleEffectSmoke.lifeSpan()
        for particleEffectLight in particleEffectArrayLightning:
            particleEffectLight.updateTimer()
            particleEffectLight.randomX()
            particleEffectLight.spawnLightning()
            particleEffectLight.checkYLocal()
            particleEffectLight.purgeLightning()
        for particleEffectRain in particleEffectArrayRain:
            particleEffectRain.update()
            particleEffectRain.updateTimer()
            particleEffectRain.spawnRain()
        for particleEffectEnergy in particleEffectArrayEnergy:
            particleEffectEnergy.update()
            particleEffectEnergy.updateTimer()
            particleEffectEnergy.spawnParticles()
            
        
    def render(self):
        for particleEffect in particleEffectArrayFire:
            particleEffect.display()
        for particleEffectSmoke in particleEffectArraySmoke:
            particleEffectSmoke.display()
        for particleEffectLight in particleEffectArrayLightning:
            particleEffectLight.display()
        for particleEffectRain in particleEffectArrayRain:
            particleEffectRain.display()
        for particleEffectEnergy in particleEffectArrayEnergy:
            particleEffectEnergy.display()
    
    def addParticleEffect(self, name, mode):
        if name == 'fire':
            if mode == 'timed':
                particleEffectArrayFire.append(ParticleEffectController(self.x,self.y,self.life))
            if mode == 'loop':
                particleEffectArrayFire.append(ParticleEffectController(self.x,self.y,99999))
        if name == 'smoke':
            if mode == 'timed':
                particleEffectArraySmoke.append(ParticleEffectController_Smoke(self.x,self.y,self.life))
            if mode == 'loop':
                particleEffectArraySmoke.append(ParticleEffectController_Smoke(self.x,self.y,99999))
        if name == 'lightning':
            if mode == 'timed' or mode == 'loop':
                particleEffectArrayLightning.append(ParticleEffectController_Lightning(self.x,self.y,30,self.life))
        if name == 'rain':
            particleEffectArrayRain.append(ParticleEffectController_Rain(self.x,self.y,99999))
        if name == 'energy':
            if mode == 'timed':
                particleEffectArrayEnergy.append(ParticleEffectController_Energy(self.x,self.y,self.life))
            if mode == 'loop':
                particleEffectArrayEnergy.append(ParticleEffectController_Energy(self.x,self.y,99999))
    def clearAll(self):
        global particleEffectArrayFire, particleEffectArraySmoke, particleEffectArrayRain, particleEffectArrayEnergy
        particleEffectArrayFire = []
        particleEffectArraySmoke = []
        particleEffectArrayRain = []
        particleEffectArrayEnergy = []
