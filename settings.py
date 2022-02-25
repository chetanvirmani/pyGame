import pygame

class settings:

    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (255,255,255)
        self.shipSpeed = 2
        self.shipLimit = 3

        #Bullet settings
        self.bulletSpeed = 1.0
        self.bulletWidth = 7
        self.bulletHeight = 15
        self.bulletColor = (60,60,60)
        self.bulletsAllowed = 3

        self.alienSpeed = 1.0
        self.fleetDropSpeed = 5
        self.fleetDirection = -1

        self.speedupScale = 1.1
        self.scoreScale = 1.5
        self.alienPoints = 50

        self.initializeDynamicSettings()
    
    def initializeDynamicSettings(self):
        self.shipSpeed = 1.2
        self.bulletSpeed = 1.0
        self.alienSpeed = 0.3
    
    def increaseSpeed(self):
        self.shipSpeed *= self.speedupScale
        self.bulletSpeed *= self.speedupScale
        self.alienSpeed *= self.speedupScale

        self.alienPoints = int(self.alienPoints * self.scoreScale)




