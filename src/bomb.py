import pygame
from src.settings import TILE_SIZE

class Bomb:
    def __init__(self, x, y, timer=60, owner=None):  # 60 frames ≈ 1 segundo com FPS=60
        self.grid_x = x
        self.grid_y = y
        self.timer = timer
        self.owner = owner
        self.image = pygame.image.load("assets/images/bomba.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self):
        self.timer -= 1
        return self.timer <= 0  # retorna True se o tempo acabou

    def draw(self, screen):
        pos = (self.grid_x * TILE_SIZE, self.grid_y * TILE_SIZE)
        screen.blit(self.image, pos)

    def explode(self, map_data, explosions):
        destroyed = []
        for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
            bx, by = self.grid_x + dx, self.grid_y + dy
            if 0 <= bx < len(map_data[0]) and 0 <= by < len(map_data):
                if map_data[by][bx] == 1:
                    continue  # parede sólida
                if map_data[by][bx] == 2:
                    map_data[by][bx] = 0
                    destroyed.append((bx, by))
                explosions.append({'x': bx, 'y': by, 'timer': 500, 'owner': self.owner})  # <- adiciona owner
        return destroyed

