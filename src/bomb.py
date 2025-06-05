import pygame
from src.settings import TILE_SIZE

class Bomb:
    def __init__(self, x, y, timer=60):  # 60 frames ≈ 1 segundo com FPS=60
        self.grid_x = x
        self.grid_y = y
        self.timer = timer
        self.image = pygame.image.load("assets/images/bomba.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def update(self):
        self.timer -= 1
        return self.timer <= 0  # retorna True se o tempo acabou

    def draw(self, screen):
        pos = (self.grid_x * TILE_SIZE, self.grid_y * TILE_SIZE)
        screen.blit(self.image, pos)
