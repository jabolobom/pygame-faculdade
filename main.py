import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MOVE_DELAY
from src.map import map_data, draw_map
from src.player import Player
from src.bomb import Bomb

explosion_img = pygame.image.load("assets/images/explosion.png")
explosion_img = pygame.transform.scale(explosion_img, (64, 64))  # Ou use TILE_SIZE se quiser


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bomberman Clone")
clock = pygame.time.Clock()

player_one = Player(1, 1, 1)
player_two = Player(9, 7, 2)

bombs = []
explosions = []
last_move_time = 0

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Coloca bomba
            if event.key == player_one.commands['place_bomb']:
                bombs.append(Bomb(player_one.grid_x, player_one.grid_y))
            if event.key == player_two.commands['place_bomb']:
                bombs.append(Bomb(player_two.grid_x, player_two.grid_y))

    # Movimento contínuo com delay
    keys = pygame.key.get_pressed()
    if current_time - last_move_time > MOVE_DELAY:
        if player_one.handle_movement(keys, map_data) or player_two.handle_movement(keys, map_data):
            last_move_time = current_time

    screen.fill((0, 0, 0))
    draw_map(screen, map_data)
    player_one.draw(screen)
    player_two.draw(screen)

    # Atualizar e desenhar bombas
    for bomb in bombs[:]:
        if bomb.update():
            # Gerar explosão
            bomb.explode(map_data, explosions)
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
        if exp['x'] == player_one.grid_x and exp['y'] == player_one.grid_y or exp['x'] == player_two.grid_x and exp['y'] == player_two.grid_y:
            print("GAME OVER: Você foi atingido pela explosão!")
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

