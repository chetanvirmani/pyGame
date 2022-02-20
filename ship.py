import pygame

class Ship:
    def __init__(self, aiGame):
        #Initializeing the ship and getting its starting position
        self.screen = aiGame.screen
        self.screen_rect = aiGame.screen.get_rect() #allows us to place the ship in the correct location on the screen

        self.image = pygame.image.load("Images/Ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #Position the ship at the center of the screen


    def blitme(self): #draws the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)
