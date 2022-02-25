import pygame.font

class Scoreboard:

    def __init__(self, aiGame):
        self.screen = aiGame.screen
        self.screenRect = self.screen.get_rect()
        self.settings = aiGame.settings
        self.stats = aiGame.stats
        self.textColor = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        self.prepScore()
    
    def prepScore(self):
        scoreStr = str(self.stats.score)
        self.scoreImage = self.font.render(scoreStr,True,self.textColor,self.settings.bg_color)
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def showScore(self):
        self.screen.blit(self.scoreImage,self.scoreRect)
