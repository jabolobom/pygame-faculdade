import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.map import map_data, draw_map
from src.player import Player
from src.bomb import Bomb  # <- Importa a bomba

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bomberman Clone")
clock = pygame.time.Clock()

player = Player(1, 1)  # posição inicial
bombs = []  # lista de bombas

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                player.handle_movement(event.key, map_data)
            elif event.key == pygame.K_SPACE:
                bombs.append(Bomb(player.grid_x, player.grid_y))

    screen.fill((0, 0, 0))
    draw_map(screen, map_data)
    player.draw(screen)

    # Atualizar e desenhar bombas
    for bomb in bombs[:]:
        if bomb.update():
            # Explodir blocos ao redor
            for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                bx = bomb.grid_x + dx
                by = bomb.grid_y + dy
                if 0 <= bx < len(map_data[0]) and 0 <= by < len(map_data):
                    if map_data[by][bx] == 2:  # bloco quebrável
                        map_data[by][bx] = 0  # transforma em chão
            bombs.remove(bomb)
        else:
            bomb.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
