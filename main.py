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

winner = None
bonus_award = None  # Jogador que causou a explosão (ganha +100)

running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Coloca bomba
            if event.key == player_one.commands['place_bomb']:
                bombs.append(Bomb(player_one.grid_x, player_one.grid_y, owner=player_one))
            if event.key == player_two.commands['place_bomb']:
                bombs.append(Bomb(player_two.grid_x, player_two.grid_y, owner=player_two))

    # Movimento contínuo com delay
    keys = pygame.key.get_pressed()
    if current_time - last_move_time > MOVE_DELAY:
        if player_one.handle_movement(keys, map_data) or player_two.handle_movement(keys, map_data):
            last_move_time = current_time

    screen.fill((0, 0, 0))
    draw_map(screen, map_data)

    player_one.draw(screen)
    player_two.draw(screen)

    player_one.update()
    player_two.update()

    # Atualizar e desenhar bombas
    for bomb in bombs[:]:
        if bomb.update():
            destroyed_blocks = bomb.explode(map_data, explosions)

            # Atribuir pontos ao jogador dono da bomba
            if bomb.owner:
                bomb.owner.add_score(len(destroyed_blocks) * 10)

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
    for exp in explosions[:]:
        owner = exp.get('owner')

        # Player 1 atingido
        if exp['x'] == player_one.grid_x and exp['y'] == player_one.grid_y:
            player_one.lives -= 1
            print(f"Player 1 perdeu uma vida! Vidas restantes: {player_one.lives}")
            if owner and owner != player_one:
                owner.add_score(100)  # +100 por cada vida tirada
            if player_one.lives > 0:
                player_one.respawn()
            else:
                winner = "Player 2"

        # Player 2 atingido
        if exp['x'] == player_two.grid_x and exp['y'] == player_two.grid_y:
            player_two.lives -= 1
            print(f"Player 2 perdeu uma vida! Vidas restantes: {player_two.lives}")
            if owner and owner != player_two:
                owner.add_score(100)  # +100 por cada vida tirada
            if player_two.lives > 0:
                player_two.respawn()
            else:
                winner = "Player 1"


    # Se alguém venceu, dar ponto e encerrar
    if winner:
        if bonus_award:
            bonus_award.add_score(100)

    # HUD com vidas e pontuação
    font = pygame.font.SysFont(None, 24)
    vida_texto_1 = font.render(f"Player 1 Vidas: {player_one.lives}", True, (0, 0, 0))
    vida_texto_2 = font.render(f"Player 2 Vidas: {player_two.lives}", True, (0, 0, 0))
    screen.blit(vida_texto_1, (10, 10))
    screen.blit(vida_texto_2, (10, 30))

    score_text_1 = font.render(f"Player 1 Pontos: {player_one.score}", True, (0, 0, 0))
    score_text_2 = font.render(f"Player 2 Pontos: {player_two.score}", True, (0, 0, 0))
    screen.blit(score_text_1, (SCREEN_WIDTH - score_text_1.get_width() - 10, 10))
    screen.blit(score_text_2, (SCREEN_WIDTH - score_text_2.get_width() - 10, 30))

    if winner:
        print(f"{winner} VENCEU!")
        pygame.display.flip()
        pygame.time.delay(3000)  # Mostra o resultado por 3 segundos
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
