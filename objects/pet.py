class Pet:

    def __init__(self, x, y, width, height, sprite_sheet):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = 1
        self.speed = 0
        self.sprite_sheet = sprite_sheet
