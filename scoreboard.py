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
        self.prepHighScore()
        self.prepLevel()
        
    def prepLevel(self):
        levelStr = str(self.stats.level)
        self.levelImage = self.font.render(levelStr, True, self.textColor, self.settings.bg_color)
        self.levelRect = self.levelImage.get_rect()
        self.levelRect.right = self.scoreRect.right
        self.levelRect.top = self.scoreRect.bottom + 10

    def prepScore(self):
        roundedScore = round (self.stats.score, -1)
        scoreStr = "{:,}".format(roundedScore)
        self.scoreImage = self.font.render(scoreStr,True,self.textColor,self.settings.bg_color)
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20
        

    def showScore(self):

        self.screen.blit(self.highScoreImage, self.highScoreRect)
        self.screen.blit(self.scoreImage,self.scoreRect)
        self.screen.blit(self.levelImage,self.levelRect)
    
    def prepHighScore(self):

        highScore = round (self.stats.highScore,-1)

        highScoreStr = "{:,}".format(highScore)
        self.highScoreImage = self.font.render(highScoreStr, True, self.textColor, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.highScoreRect = self.highScoreImage.get_rect()
        self.highScoreRect.centerx = self.screenRect.centerx
        self.highScoreRect.top = self.scoreRect.top

    def checkHighScore(self):

        openHighScoreFile = open("highScoreData.txt","r")
        self.stats.highScore = int(openHighScoreFile.readline())
        openHighScoreFile.close

        self.prepHighScore()
        
        if self.stats.score >= (self.stats.highScore):
            self.stats.highScore = self.stats.score
            self.prepHighScore()
        
        
        writeHighScore = open("highScoreData.txt","w")
        writeHighScore.write(str(self.stats.highScore))
        writeHighScore.close()
    