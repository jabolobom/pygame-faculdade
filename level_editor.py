import pygame, json
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_SIZE
from src.map import draw_map
from datetime import datetime
from src.main_menu import InputBox

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

def save_map(map_name, map_array):
    filename = map_name + ".json"  # placeholder, intenção é permitir o usuário nomear o mapa resultante
    with open(filename, "w") as f:
        json.dump(map_array, f)
        f.close()
    pygame.quit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor') # dá pra mudar mais tarde e rodar junto com o programa principal, talvez um main menu com escolha entre jogo e editor
clock = pygame.time.Clock()

renamebox = InputBox(100, 100, TILE_SIZE, TILE_SIZE)
working_map = map_selection(empty_map)  # escolhe o mapa a ser editado
# tudo dentro do mesmo programa...

running = True
while running:

    current_time = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if renamebox.active:
            mapname = renamebox.handle_event(event)
            if mapname:
                save_map(mapname, working_map)

        if event.type == pygame.MOUSEBUTTONDOWN: # handling da posição de cada clique
            x,y = pygame.mouse.get_pos()
            colclick = x // TILE_SIZE
            rowclick = y // TILE_SIZE
            print(f"click em {colclick} e {rowclick}")
            if 0 <= rowclick < len(working_map) and 0 <= colclick < len(working_map[0]):
                if working_map[rowclick][colclick] < 2:
                        working_map[rowclick][colclick] += 1
                else:
                        working_map[rowclick][colclick] = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if not renamebox.active:
                    renamebox.active = True

    draw_map(screen, working_map)
    if renamebox.active:
        renamebox.update()
        renamebox.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()