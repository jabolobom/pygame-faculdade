import pygame
from src.settings import TILE_SIZE

class Player:
    def __init__(self, x, y):
        self.grid_x = x
        self.grid_y = y
        self.image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

    def handle_movement(self, key, map_data):
        new_x, new_y = self.grid_x, self.grid_y

        if key == pygame.K_LEFT:
            new_x -= 1
        elif key == pygame.K_RIGHT:  
            new_x += 1
        elif key == pygame.K_UP:
            new_y -= 1
        elif key == pygame.K_DOWN:
            new_y += 1

        # Verifica limites e colisão
        if 0 <= new_x < len(map_data[0]) and 0 <= new_y < len(map_data):
            if map_data[new_y][new_x] == 0:
                self.grid_x, self.grid_y = new_x, new_y

    def draw(self, screen):
        pos = (self.grid_x * TILE_SIZE, self.grid_y * TILE_SIZE)
        screen.blit(self.image, pos)
