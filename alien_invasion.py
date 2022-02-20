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

        self.bg_color = (230,230,230)

    
    def runGame(self):
        run = True
        while run:

            for event in pygame.event.get(): #event is a press of a key by the user
                if event.type == pygame.QUIT: #We'll write different IF statements to figure out the type of event the user requested
                    run = False #When player clicks the close window button, this will kick in and the game will be exited
            
            
            self.screen.fill(self.settings.bg_color)

            self.ship.blitme() #Ship appears on top of the background

            pygame.display.flip() #makes the most recently drawn screen visible, so in the while loop it continously displays the results of events


if __name__ == "__main__":
    ai = alienInvasion()
    ai.runGame


