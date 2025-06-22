import pygame

FPS = 60
TILE_SIZE = 64
SCREEN_WIDTH = 11 * TILE_SIZE # Ajuste conforme o tamanho do mapa e TILE_SIZE
SCREEN_HEIGHT = 9 * TILE_SIZE
PREMADE_MAP_PATH = "assets/maps/premade"
USER_MAP_PATH = "assets/maps/usermade"
FONT_PATH = "assets/font.ttf"


VOLUME_BAR_WIDTH = SCREEN_WIDTH // 8
VOLUME_BAR_HEIGHT = 10
MUTE_BUTTON_WIDTH = SCREEN_WIDTH // 30
MUTE_BUTTON_HEIGHT = MUTE_BUTTON_WIDTH
VOLUME_BAR_WIDTH = SCREEN_WIDTH // 8
VOLUME_BAR_HEIGHT = MUTE_BUTTON_HEIGHT // 4
VOLUME_KNOB_RADIUS = (VOLUME_BAR_HEIGHT // 2) * 3
AUDIO_HUD_Y = 20
TOTAL_AUDIO_HUD_WIDTH = VOLUME_BAR_WIDTH + 10 + MUTE_BUTTON_WIDTH 
AUDIO_HUD_START_X = (SCREEN_WIDTH // 2) - (TOTAL_AUDIO_HUD_WIDTH // 2)
MUTE_BUTTON_X = AUDIO_HUD_START_X
MUTE_BUTTON_Y = AUDIO_HUD_Y + (VOLUME_BAR_HEIGHT // 2) - (MUTE_BUTTON_HEIGHT // 2)
VOLUME_BAR_X = MUTE_BUTTON_X + MUTE_BUTTON_WIDTH + 10
VOLUME_BAR_Y = AUDIO_HUD_Y


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

VOLUME_HUD = {
    "VOLUME_BAR_WIDTH": VOLUME_BAR_WIDTH,
    "VOLUME_BAR_HEIGHT": VOLUME_BAR_HEIGHT,
    "MUTE_BUTTON_WIDTH": MUTE_BUTTON_WIDTH,
    "MUTE_BUTTON_HEIGHT": MUTE_BUTTON_HEIGHT,
    "VOLUME_BAR_X": VOLUME_BAR_X,
    "VOLUME_BAR_Y": VOLUME_BAR_Y,
    "MUTE_BUTTON_X": MUTE_BUTTON_X,
    "MUTE_BUTTON_Y": MUTE_BUTTON_Y,
    "VOLUME_KNOB_RADIUS": VOLUME_KNOB_RADIUS
}

# Delay para movimento contínuo
# zerei o delay para não conflitar a movimentação entre os jogadores
MOVE_DELAY = 0  # milissegundos