import pygame
from src.settings import TILE_SIZE, PLAYER_ONE_COMMANDS, PLAYER_TWO_COMMANDS

class Player:
    def __init__(self, x, y, player_id=1):
        self.grid_x = x
        self.grid_y = y
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.direction = "down"
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 120  # ms entre quadros
        self.moving = False
        self.initial_x = x
        self.initial_y = y
        self.lives = 3  # Número inicial de vidas
        self.move_speed = 4  # pixels por frame

        # Carrega animações para cada direção
        self.animations = {
            "down": [pygame.transform.scale(pygame.image.load(f"assets/images/bombermanSprites/player_down_{i}.png"), (TILE_SIZE, TILE_SIZE)) for i in range(2)],
            "up": [pygame.transform.scale(pygame.image.load(f"assets/images/bombermanSprites/player_up_{i}.png"), (TILE_SIZE, TILE_SIZE)) for i in range(2)],
            "left": [pygame.transform.scale(pygame.image.load(f"assets/images/bombermanSprites/player_left_{i}.png"), (TILE_SIZE, TILE_SIZE)) for i in range(2)],
            "right": [pygame.transform.scale(pygame.image.load(f"assets/images/bombermanSprites/player_right_{i}.png"), (TILE_SIZE, TILE_SIZE)) for i in range(2)],
        }
        self.image = self.animations["down"][0]

        if player_id == 2:
            self.commands = PLAYER_TWO_COMMANDS
        else:
            self.commands = PLAYER_ONE_COMMANDS

    def handle_movement(self, keys, map_data):
        if self.moving:
            return False  # Já está se movendo

        new_x, new_y = self.grid_x, self.grid_y

        if keys[self.commands["left"]]:
            new_x -= 1
            self.direction = "left"
        elif keys[self.commands["right"]]:
            new_x += 1
            self.direction = "right"
        elif keys[self.commands["up"]]:
            new_y -= 1
            self.direction = "up"
        elif keys[self.commands["down"]]:
            new_y += 1
            self.direction = "down"
        else:
            return False  # Nenhuma tecla pressionada

        # Verifica limites e colisão
        if 0 <= new_x < len(map_data[0]) and 0 <= new_y < len(map_data):
            if map_data[new_y][new_x] == 0:
                self.grid_x, self.grid_y = new_x, new_y
                self.moving = True
                return True

        return False

    def update(self):
        # Movimento suave
        target_x = self.grid_x * TILE_SIZE
        target_y = self.grid_y * TILE_SIZE

        if self.moving:
            dx = target_x - self.x
            dy = target_y - self.y

            if abs(dx) > self.move_speed:
                self.x += self.move_speed if dx > 0 else -self.move_speed
            else:
                self.x = target_x

            if abs(dy) > self.move_speed:
                self.y += self.move_speed if dy > 0 else -self.move_speed
            else:
                self.y = target_y

            if self.x == target_x and self.y == target_y:
                self.moving = False

            self.update_animation()
        else:
            self.frame_index = 0
            self.image = self.animations[self.direction][0]

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.frame_index = (self.frame_index + 1) % len(self.animations[self.direction])
            self.image = self.animations[self.direction][self.frame_index]
            self.last_update = now

    def draw(self, screen):
        pos = (int(self.x), int(self.y))
        screen.blit(self.image, pos)

    def respawn(self):
        self.grid_x = self.initial_x
        self.grid_y = self.initial_y
        self.x = self.grid_x * TILE_SIZE
        self.y = self.grid_y * TILE_SIZE
        self.moving = False
        self.direction = "down"