class GameStats:
    def __init__(self, aiGame):
        self.settings = aiGame.settings
        self.resetStats()
        self.gameActive = False

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit