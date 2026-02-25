from sprites import Sprite
from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self, width, height, bg_tile = None):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector(500,0)
        self.width = width * TILE_SIZE
        self.height = height * TILE_SIZE
        self.borders ={
            'left': 0,
            'right': -self.width + WINDOW_WIDTH,
            'bottom': -self.height + WINDOW_HEIGHT,
            'top': 0
        }

        if bg_tile:
            for col in range(width):
                for row in range(height):
                    x, y = col * TILE_SIZE, row * TILE_SIZE
                    Sprite((x, y), bg_tile, self, -1)

    def camera_constraint(self):
        self.offset.x = self.offset.x if self.offset.x < 0 else 0
        self.offset.x = self.offset.x if self.offset.x > self.borders['right'] else self.borders['right']
        self.offset.y = self.offset.y if self.offset.y < 0 else 0
        self.offset.y = self.offset.y if self.offset.y > self.borders['bottom'] else self.borders['bottom']

    def draw(self, target_position):
        self.offset.x = -(target_position[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_position[1] - WINDOW_HEIGHT / 2)
        self.camera_constraint()
        
        for sprite in sorted(self, key = lambda sprite: sprite.z):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)