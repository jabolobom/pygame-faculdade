import pygame
from src.settings import TILE_SIZE

map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Carregando as imagens dos blocos
floor = pygame.image.load("assets/images/floor.jfif")
solid_block = pygame.image.load("assets/images/block_solid.jpg")
breakable_block = pygame.image.load("assets/images/block_breakable.jfif")

# Ajustar o tamanho das imagens
floor = pygame.transform.scale(floor, (TILE_SIZE, TILE_SIZE))
solid_block = pygame.transform.scale(solid_block, (TILE_SIZE, TILE_SIZE))
breakable_block = pygame.transform.scale(breakable_block, (TILE_SIZE, TILE_SIZE))

def draw_map(screen, selected_map):
    for y, row in enumerate(selected_map):
        for x, tile in enumerate(row):
            pos = (x * TILE_SIZE, y * TILE_SIZE)
            screen.blit(floor, pos)  # chão sempre desenhado por baixo
            if tile == 1:
                screen.blit(solid_block, pos)
            elif tile == 2:
                screen.blit(breakable_block, pos)
