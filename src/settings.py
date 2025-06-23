import pygame

FPS = 60
TILE_SIZE = 64
SCREEN_WIDTH = 11 * TILE_SIZE # Ajuste conforme o tamanho do mapa e TILE_SIZE
SCREEN_HEIGHT = 9 * TILE_SIZE
PREMADE_MAP_PATH = "assets/maps/premade"
USER_MAP_PATH = "assets/maps/usermade"
FONT_PATH = "assets/font.ttf"



PLAYER_ONE_COMMANDS = {
    "up": pygame.K_w,
    "down": pygame.K_s,
    "left": pygame.K_a,
    "right": pygame.K_d,
    "place_bomb": pygame.K_q
}

PLAYER_TWO_COMMANDS = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "place_bomb": pygame.K_RETURN
}

# Delay para movimento contínuo
# zerei o delay para não conflitar a movimentação entre os jogadores
MOVE_DELAY = 0  # milissegundos


