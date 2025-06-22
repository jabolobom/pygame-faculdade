import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MOVE_DELAY, VOLUME_HUD
from src.map import draw_map
from src.player import Player
from src.bomb import Bomb
from src.audio import Audio

def run(map_data):
    def count_remaining_destructibles(map_data):
        return sum(row.count(2) for row in map_data)

    explosion_img = pygame.image.load("assets/images/explosion.png")
    explosion_img = pygame.transform.scale(explosion_img, (64, 64))  # Ou use TILE_SIZE


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bomberman Clone")
    clock = pygame.time.Clock()

    audio = Audio("assets/audio/fight_music.mp3")

    player_one = Player(1, 1, 1)
    player_two = Player(9, 7, 2)

    bombs = []
    explosions = []
    last_move_time = 0

    winner = None

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN and not winner:
                if event.key == player_one.commands['place_bomb']:
                    bombs.append(Bomb(player_one.grid_x, player_one.grid_y, owner=player_one))
                if event.key == player_two.commands['place_bomb']:
                    bombs.append(Bomb(player_two.grid_x, player_two.grid_y, owner=player_two))

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                if audio.volume_bar_rect.collidepoint(mouse_x, mouse_y):
                    audio.set_volume(mouse_x)

                if audio.mute_button_rect.collidepoint(mouse_x, mouse_y):
                    audio.mute_unmute()

        if not winner:
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

        if not winner:
            for bomb in bombs[:]:
                if bomb.update():
                    destroyed_blocks = bomb.explode(map_data, explosions)
                    if bomb.owner:
                        bomb.owner.add_score(len(destroyed_blocks) * 10)
                    bombs.remove(bomb)
                else:
                    bomb.draw(screen)

        for exp in explosions[:]:
            screen.blit(explosion_img, (exp['x'] * 64, exp['y'] * 64))
            exp['timer'] -= clock.get_time()
            if exp['timer'] <= 0:
                explosions.remove(exp)

        if not winner:
            for exp in explosions[:]:
                owner = exp.get('owner')
                if exp['x'] == player_one.grid_x and exp['y'] == player_one.grid_y:
                    player_one.lives -= 1
                    print(f"Player 1 perdeu uma vida! Vidas restantes: {player_one.lives}")
                    if owner and owner != player_one:
                        owner.add_score(100)
                    if player_one.lives > 0:
                        player_one.respawn()

                if exp['x'] == player_two.grid_x and exp['y'] == player_two.grid_y:
                    player_two.lives -= 1
                    print(f"Player 2 perdeu uma vida! Vidas restantes: {player_two.lives}")
                    if owner and owner != player_two:
                        owner.add_score(100)
                    if player_two.lives > 0:
                        player_two.respawn()

            # Verificar condições de fim de jogo
            if player_one.lives <= 0 or player_two.lives <= 0 or count_remaining_destructibles(map_data) == 0:
                if player_one.score > player_two.score:
                    winner = "Player 1"
                elif player_two.score > player_one.score:
                    winner = "Player 2"
                else:
                    winner = "Empate"

        # HUD
        font = pygame.font.SysFont(None, 24)
        vida_texto_1 = font.render(f"Player 1 Vidas: {player_one.lives}", True, (0, 0, 0))
        vida_texto_2 = font.render(f"Player 2 Vidas: {player_two.lives}", True, (0, 0, 0))
        score_text_1 = font.render(f"Player 1 Pontos: {player_one.score}", True, (0, 0, 0))
        score_text_2 = font.render(f"Player 2 Pontos: {player_two.score}", True, (0, 0, 0))

        screen.blit(vida_texto_1, (10, 10))
        screen.blit(vida_texto_2, (10, 30))
        screen.blit(score_text_1, (SCREEN_WIDTH - score_text_1.get_width() - 10, 10))
        screen.blit(score_text_2, (SCREEN_WIDTH - score_text_2.get_width() - 10, 30))

        audio.draw_volume_bar(screen)
        audio.draw_mute_button(screen)

        # bar_rect = pygame.Rect(VOLUME_HUD['VOLUME_BAR_X'], VOLUME_HUD['VOLUME_BAR_Y'], VOLUME_HUD['VOLUME_BAR_WIDTH'], VOLUME_HUD['VOLUME_BAR_HEIGHT'])
        # pygame.draw.rect(screen, (0, 0, 0), bar_rect, 0, border_radius=5)
        # knob_x = VOLUME_HUD['VOLUME_BAR_X'] + int(current_volume * VOLUME_HUD['VOLUME_BAR_WIDTH'])
        # knob_y = VOLUME_HUD['VOLUME_BAR_Y'] + (VOLUME_HUD['VOLUME_BAR_HEIGHT'] // 2)
        # pygame.draw.circle(screen, (0, 0, 0), (knob_x, knob_y), VOLUME_HUD['VOLUME_KNOB_RADIUS'])

        # screen.blit(music_note_img, (VOLUME_HUD['MUTE_BUTTON_X'], VOLUME_HUD['MUTE_BUTTON_Y']))

        # if is_muted:
        #     bar_color = (255, 0, 0)
        #     start_pos = (VOLUME_HUD['MUTE_BUTTON_X'], VOLUME_HUD['MUTE_BUTTON_Y'] + VOLUME_HUD['MUTE_BUTTON_HEIGHT'])
        #     end_pos = (VOLUME_HUD['MUTE_BUTTON_X'] + VOLUME_HUD['MUTE_BUTTON_WIDTH'], VOLUME_HUD['MUTE_BUTTON_Y'])
        #     pygame.draw.line(screen, bar_color, start_pos, end_pos, 5)

        if winner:
            # Mensagem centralizada
            victory_text = font.render(f"{winner} venceu!", True, (255, 0, 0))
            victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))

            # Delay com renderização final
            victory_start = pygame.time.get_ticks()
            while pygame.time.get_ticks() - victory_start < 3000:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                screen.fill((0, 0, 0))
                draw_map(screen, map_data)
                player_one.draw(screen)
                player_two.draw(screen)
                screen.blit(score_text_1, (SCREEN_WIDTH - score_text_1.get_width() - 10, 10))
                screen.blit(score_text_2, (SCREEN_WIDTH - score_text_2.get_width() - 10, 30))
                screen.blit(vida_texto_1, (10, 10))
                screen.blit(vida_texto_2, (10, 30))
                screen.blit(victory_text, victory_rect)
                pygame.display.flip()
                clock.tick(FPS)

            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
