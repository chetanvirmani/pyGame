import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, aiGame):
        super().__init__()
        self.screen = aiGame.screen

        self.image = pygame.image.load("Images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width #Start each new alien near the top left of the screen
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

