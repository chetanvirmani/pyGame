class GameStats:
    def __init__(self, aiGame):
        self.settings = aiGame.settings
        self.resetStats()
        self.gameActive = True

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit