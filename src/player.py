import pygame
from src.settings import TILE_SIZE, PLAYER_ONE_COMMANDS, PLAYER_TWO_COMMANDS

class Player:
    def __init__(self, x, y, player_id=1):
        self.grid_x = x
        self.grid_y = y
        self.image = pygame.image.load("assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        if player_id == 2:
            self.commands = PLAYER_TWO_COMMANDS
        else:
            self.commands = PLAYER_ONE_COMMANDS

    def handle_movement(self, keys, map_data):
        new_x, new_y = self.grid_x, self.grid_y

        if keys[self.commands["left"]]:
            new_x -= 1
        elif keys[self.commands["right"]]:
            new_x += 1
        elif keys[self.commands["up"]]:
            new_y -= 1
        elif keys[self.commands["down"]]:
            new_y += 1
        else:
            return False  # Nenhuma tecla pressionada

        # Verifica limites e colisão
        if 0 <= new_x < len(map_data[0]) and 0 <= new_y < len(map_data):
            if map_data[new_y][new_x] == 0:
                self.grid_x, self.grid_y = new_x, new_y
                return True

        return False

    def draw(self, screen):
        pos = (self.grid_x * TILE_SIZE, self.grid_y * TILE_SIZE)
        screen.blit(self.image, pos)
