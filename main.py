import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.map import map_data, draw_map
from src.player import Player
from src.bomb import Bomb

explosion_img = pygame.image.load("assets/images/explosion.png")
explosion_img = pygame.transform.scale(explosion_img, (64, 64))  # Ou use TILE_SIZE se quiser


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bomberman Clone")
clock = pygame.time.Clock()

player = Player(1, 1)
bombs = []
explosions = []

# Delay para movimento contínuo
MOVE_DELAY = 150  # milissegundos
last_move_time = 0

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Coloca bomba com espaço
            if event.key == pygame.K_SPACE:
                bombs.append(Bomb(player.grid_x, player.grid_y))

    # Movimento contínuo com delay
    keys = pygame.key.get_pressed()
    if current_time - last_move_time > MOVE_DELAY:
        if player.handle_movement(keys, map_data):
            last_move_time = current_time

    screen.fill((0, 0, 0))
    draw_map(screen, map_data)
    player.draw(screen)

    # Atualizar e desenhar bombas
    for bomb in bombs[:]:
        if bomb.update():
            # Gerar explosão
            for dx, dy in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                bx, by = bomb.grid_x + dx, bomb.grid_y + dy
                if 0 <= bx < len(map_data[0]) and 0 <= by < len(map_data):
                    if map_data[by][bx] == 1:
                        continue  # parede sólida, não explode nem passa
                    if map_data[by][bx] == 2:
                        map_data[by][bx] = 0  # destrói bloco
                    explosions.append({'x': bx, 'y': by, 'timer': 500})
            bombs.remove(bomb)
        else:
            bomb.draw(screen)

    # Atualizar e desenhar explosões
    for exp in explosions[:]:
        screen.blit(explosion_img, (exp['x'] * 64, exp['y'] * 64))  # Ou use TILE_SIZE
        exp['timer'] -= clock.get_time()
        if exp['timer'] <= 0:
            explosions.remove(exp)

    # Verificar se jogador colidiu com explosão
    for exp in explosions:
        if exp['x'] == player.grid_x and exp['y'] == player.grid_y:
            print("GAME OVER: Você foi atingido pela explosão!")
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

