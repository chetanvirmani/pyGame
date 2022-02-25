class GameStats:
    def __init__(self, aiGame):
        self.settings = aiGame.settings
        self.resetStats()
        self.gameActive = False

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0 #We are initializing the score here rather than def because we want to reset the score each time a new game starts
        