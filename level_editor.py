import pygame, json
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_SIZE
from src.map import draw_map
from datetime import datetime

empty_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def map_selection(maplist):
    return maplist # nõa faz nada, PLACEHOLDER!!!!!!

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor') # dá pra mudar mais tarde e rodar
clock = pygame.time.Clock()

working_map = map_selection(empty_map)  # escolhe o mapa a ser editado

# tudo dentro do mesmo programa...

running = True
while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            colclick = x // TILE_SIZE
            rowclick = y // TILE_SIZE
            print(f"click em {colclick} e {rowclick}")
            if working_map[rowclick][colclick] < 2:
                working_map[rowclick][colclick] += 1
            else:
                working_map[rowclick][colclick] = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                final_map = working_map
                filename = datetime.now().strftime("%Y-%m-%d %H%M%S") + "_map" + ".json"
                with open(filename, "w") as f:
                    json.dump(final_map, f)
                    f.close()
                pygame.quit()

    draw_map(screen, working_map)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()