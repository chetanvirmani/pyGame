import sys
import pygame
from settings import settings
from ship import Ship



class alienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = settings()

        # pygame.display.set_mode() is a surface - a surface is a part of screen where the game elements will be displayed
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #Create an instance of the ship after the screen has been created

        self.bg_color = (self.settings.bg_color)



    def runGame(self):

        while True:

            self.checkEvents()
            self.ship.update()
            self.updateScreen()

            

    def checkEvents(self): #Respond to keypresses and mouse events

        for event in pygame.event.get(): #event is a press of a key by the user
            if event.type == pygame.QUIT: #We'll write different IF statements to figure out the type of event the user requested
                sys.exit() #When player clicks the close window button, this will kick in and the game will be exited
            
            elif event.type == pygame.KEYDOWN:
                self.checkKeydownEvents(event)
            
            elif event.type == pygame.KEYUP:
                self.checkKeyupEvents(event)
        
    
    def updateScreen(self):
    
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #Ship appears on top of the background
        pygame.display.flip() #makes the most recently drawn screen visible, so in the while loop it continously displays the results of events

    def checkKeydownEvents (self, event):
        if event.key == pygame.K_RIGHT: #Checking for the key type
            self.ship.movingRight = True #Move the ship along the x axis
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()

    
    def checkKeyupEvents (self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False

