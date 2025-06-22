import json
import pygame, os
from src.settings import TILE_SIZE, PREMADE_MAP_PATH, USER_MAP_PATH

# Carregando as imagens dos blocos
floor = pygame.image.load("assets/images/floor.jfif")
solid_block = pygame.image.load("assets/images/block_solid.jpg")
breakable_block = pygame.image.load("assets/images/block_breakable.jpg")

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

def count_remaining_destructibles(map_data):
    count = 0
    for row in map_data:
        count += row.count(2)  # 2 representa bloco destrutível
    return count