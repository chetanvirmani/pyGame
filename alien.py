import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, aiGame):
        super().__init__()
        self.screen = aiGame.screen

        self.image = pygame.image.load("Images/alien.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width #Start each new alien near the top left of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.settings = aiGame.settings
    
    def update(self):
        self.x += (self.settings.alienSpeed * self.settings.fleetDirection) #the fleet direction basically makes the result positive or negative
        self.rect.x = self.x
    
    def checkEdges(self):
        screenRect = self.screen.get_rect()
        if self.rect.right >= screenRect.right or self.rect.left <= 0:
            return True
            

