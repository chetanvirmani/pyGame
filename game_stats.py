class GameStats:
    def __init__(self, aiGame):
        self.settings = aiGame.settings
        self.resetStats()
        self.gameActive = False
        self.highScore = 0 #this is in init because we never want to reset the high score
        self.level = 1


    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0 #We are initializing the score here rather than def because we want to reset the score each time a new game starts
