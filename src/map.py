import json
import pygame, os
from src.settings import TILE_SIZE, PREMADE_MAP_PATH, USER_MAP_PATH

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

def map_loader(ppath, upath): # basicamente o ESQUELETO da função, placeholder ao extremo, precisamos do main menu pra definir
    # como terminar essa parte.

    # no momento vai funcionar dentro do terminal...
    maplist = list()
    is_map_selected = False

    while not is_map_selected: # ATENÇÃO, NÃO TEM CHECK DE ERRO !!!NENHUM!!! o programa VAI QUEBRAR se digitar algo não intencional...
        choice = input("Escolha 1: Mapas Premade; 2: Mapas de usuários\n>")
        match choice:
            case "1":
                for name in os.listdir(ppath):
                    if name.endswith(".json"):
                        maplist.append(name)
                try:
                    for i, name in enumerate(maplist):
                        print(f"Mapa {i}: {name}")

                    mapchoice = int(input("Escolha o mapa através do index: "))
                except ValueError:
                    print("Invalid choice")

                if maplist[mapchoice]:

                    is_map_selected = True
                    filepath = os.path.join(ppath, maplist[mapchoice])

                    with open(filepath, "r") as f:
                        loaded_map = json.load(f)
                        f.close()
                    return loaded_map

            case "2":
                for name in os.listdir(upath):
                    if name.endswith(".json"):
                        print(f"Map: {name}")
                        maplist.append(name)
                try:
                    for i, name in enumerate(maplist):
                        print(f"Mapa {i}: {name}")

                    mapchoice = int(input("Escolha o mapa através do index: "))
                except ValueError:
                    print("Invalid choice")

                if maplist[mapchoice]:

                    is_map_selected = True
                    filepath = os.path.join(upath, maplist[mapchoice])

                    with open(filepath, "r") as f:
                        loaded_map = json.load(f)
                        f.close()
                    return loaded_map

            case _:
                print("opção inválida")

    return None

def count_remaining_destructibles(map_data):
    count = 0
    for row in map_data:
        count += row.count(2)  # 2 representa bloco destrutível
    return count


map_data = map_loader(PREMADE_MAP_PATH, USER_MAP_PATH)