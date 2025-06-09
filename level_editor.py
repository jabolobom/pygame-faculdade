import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_SIZE
from src.map import map_data, draw_map

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor') # dá pra mudar mais tarde e rodar
# tudo dentro do mesmo programa...

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            colclick = x // TILE_SIZE
            rowclick = y // TILE_SIZE
            print(f"click em {colclick} e {rowclick}")
            if map_data[colclick][rowclick] < 2:
                map_data[colclick][rowclick] += 1
            else:
                map_data[colclick][rowclick] = 0

    draw_map(screen, map_data)