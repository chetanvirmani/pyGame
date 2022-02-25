import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, aiGame):
        super().__init__()
        #Initializeing the ship and getting its starting position
        self.screen = aiGame.screen
        self.settings = aiGame.settings
        self.screen_rect = aiGame.screen.get_rect() #allows us to place the ship in the correct location on the screen

        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #Position the ship at the center of the screen

        self.movingRight = False
        self.movingLeft = False

        self.x = float(self.rect.x)
    
    


    def blitme(self): #draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.movingRight and self.rect.right < self.screen_rect.right:
            self.x += self.settings.shipSpeed #Keep moving right as long as movingRight is True
            
        
        if self.movingLeft and self.rect.left > 0: 
            self.x -= self.settings.shipSpeed
        
        self.rect.x = self.x
    
    def centerShip(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

