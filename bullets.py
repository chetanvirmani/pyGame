import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, aiGame):

        super().__init__() #A bit confused about super and sprite
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.color = aiGame.settings.bulletColor

        self.rect = pygame.Rect(0,0,self.settings.bulletWidth,self.settings.bulletHeight)
        self.rect.midtop = aiGame.ship.rect.midtop
        self.y = float(self.rect.y)
    
    def update (self):
        self.y -= self.settings.bulletSpeed #we subtract value from y to make it seem like the bullet is going upwards
        self.rect.y = self.y #the higher the speed, the faster the number will subtract
    
    def drawBullet (self):
        pygame.draw.rect(self.screen,self.color, self.rect)