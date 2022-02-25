class settings:

    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (230,230,230)
        self.shipSpeed = 1.2
        self.shipLimit = 1

        #Bullet settings
        self.bulletSpeed = 1.0
        self.bulletWidth = 20
        self.bulletHeight = 15
        self.bulletColor = (60,60,60)
        self.bulletsAllowed = 3

        self.alienSpeed = 1.0
        self.fleetDropSpeed = 5
        self.fleetDirection = -1

        self.speedupScale = 1.1

        self.initializeDynamicSettings()
    
    def initializeDynamicSettings(self):
        self.shipSpeed = 1.2
        self.bulletSpeed = 1.0
        self.alienSpeed = 1.0
    
    def increaseSpeed(self):
        self.shipSpeed *= self.speedupScale
        self.bulletSpeed *= self.speedupScale
        self.alienSpeed *= self.speedupScale




