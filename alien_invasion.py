from pickle import FALSE
import sys
import pygame
from settings import settings
from ship import Ship



class alienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = settings()

        # pygame.display.set_mode() is a surface - a surface is a part of screen where the game elements will be displayed
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) #Create an instance of the ship after the screen has been created

        self.bg_color = (self.settings.bg_color)



    def runGame(self):

        while True:

            #self.checkEvents()
            self.ship.update()
            #def checkEvents(self): #Respond to keypresses and mouse events
            for event in pygame.event.get(): #event is a press of a key by the user
                if event.type == pygame.QUIT: #We'll write different IF statements to figure out the type of event the user requested
                    sys.exit() #When player clicks the close window button, this will kick in and the game will be exited
                
                elif event.type == pygame.KEYDOWN: #If the user has pressed a key
                    if event.key == pygame.K_RIGHT: #Checking for the key type
                        self.ship.movingRight = True #Move the ship along the x axis
                
                elif event.type  == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.movingRight = False




            #self.updateScreen()

            #def updateScreen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme() #Ship appears on top of the background
            pygame.display.flip() #makes the most recently drawn screen visible, so in the while loop it continously displays the results of events

            
            


