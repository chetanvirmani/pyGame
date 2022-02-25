import sys
from time import sleep
import pygame
from settings import settings
from game_stats import GameStats
from ship import Ship
from bullets import Bullet
from alien import Alien
from button import Button



class alienInvasion:

    def __init__(self):

        pygame.init()
        self.settings = settings()

        # pygame.display.set_mode() is a surface - a surface is a part of screen where the game elements will be displayed
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width #by doing this we are disregarding the settings, and just going for full screen
        self.settings.screen_height = self.screen.get_rect().height
        self.bg_color = (self.settings.bg_color)

        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.ship = Ship(self) #Create an instance of the ship after the screen has been created
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group() #Read more

        self.createFleet()

        self.playButton = Button(self, "Play")

        



    def runGame(self):

        while True:

            self.checkEvents()

            if self.stats.gameActive:

                self.ship.update()
                self.bullets.update() #calling the update function in bullets
                self.updateAliens()
                self.updateBullets()
                
            self.updateScreen()

            


    def updateBullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self.createFleet()


    def checkEvents(self): #Respond to keypresses and mouse events

        for event in pygame.event.get(): #event is a press of a key by the user
            if event.type == pygame.QUIT: #We'll write different IF statements to figure out the type of event the user requested
                sys.exit() #When player clicks the close window button, this will kick in and the game will be exited
            
            elif event.type == pygame.KEYDOWN:
                self.checkKeydownEvents(event)
            
            elif event.type == pygame.KEYUP:
                self.checkKeyupEvents(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                self.checkPlayButton(mousePosition)
        
    def checkPlayButton (self, mousePosition):
        buttonClicked = self.playButton.rect.collidepoint(mousePosition)
        
        if buttonClicked and not self.stats.gameActive:
            self.stats.resetStats()
            self.stats.gameActive = True

            """
            self.bullets.empty()
            self.aliens.empty()

            self.createFleet
            self.ship.centerShip()
            """
        
            pygame.mouse.set_visible(False)

        
    
    def updateScreen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() #Ship appears on top of the background
        
        for bullet in self.bullets.sprites():
            bullet.drawBullet()
        

        
        
        self.aliens.draw(self.screen)

        if not self.stats.gameActive:
            self.playButton.drawButton()

        pygame.display.flip() #makes the most recently drawn screen visible, so in the while loop it continously displays the results of events
        
        

    def checkKeydownEvents (self, event):
        if event.key == pygame.K_RIGHT: #Checking for the key type
            self.ship.movingRight = True #Move the ship along the x axis
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fireBullet()
        elif event.key == pygame.K_b:
            if self.settings.bulletWidth != 300:
                self.settings.bulletWidth = 300
            else:
                self.settings.bulletWidth = 20

    
    def checkKeyupEvents (self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.movingRight = False
        elif event.key == pygame.K_LEFT:
            self.ship.movingLeft = False

    def fireBullet(self):
        if len(self.bullets) < self.settings.bulletsAllowed:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
        

    def createFleet(self):
        alien = Alien(self) #Referencing from the alien file
        alienWidth, alienHeight = alien.rect.size
        availableSpaceX = self.settings.screen_width - (2 * alienWidth)
        numberAliensX = availableSpaceX // (2*alienWidth)
        
        shipHeight = self.ship.rect.height
        availableSpaceY = (self.settings.screen_height - (3 * alienHeight) - shipHeight)

        numberRows = availableSpaceY // (2 * alienHeight)

        for rowNumber in range(numberRows):
            for alienNumber in range (numberAliensX):
                self.createAlien(alienNumber, rowNumber, alienWidth, alienHeight)

      
    def createAlien(self,alienNumber,rowNumber, alienWidth, alienHeight):
        alien = Alien(self)
        alien.x = alienWidth + 2 * alienWidth * alienNumber
        alien.y = alienHeight + 10 + rowNumber * alienHeight * 2
        alien.rect.x = alien.x
        alien.rect.y = alien.y

        self.aliens.add(alien)
    
    def updateAliens (self):
        self.checkFleetEdges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("ship hit")
            self.shipHit()
        self.checkAliensBottom()
        

    def checkFleetEdges (self):
        for alien in self.aliens.sprites():
            if alien.checkEdges():
                self.changeFleetDirection()
                break
    
    def changeFleetDirection (self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleetDropSpeed
        self.settings.fleetDirection *= -1
        
    def shipHit(self):

        if self.stats.shipsLeft > 0:

            self.stats.shipsLeft -= 1
            self.aliens.empty()
            self.bullets.empty()

            self.createFleet()
            self.ship.centerShip()

            sleep(0.5)

        else:

            self.stats.gameActive = False
            pygame.mouse.set_visible(True)


    
    def checkAliensBottom(self):
        screenRect = self.screen.get_rect()
        
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screenRect.bottom:
                print ("Ship hit")
                self.shipHit()
                break
        