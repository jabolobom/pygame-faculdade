import os

import pygame, json
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TILE_SIZE, USER_MAP_PATH, FONT_PATH
from src.map import draw_map
from datetime import datetime
from src.input_box import InputBox
from src.buttons import Buttons
from main import load_map, get_font



def save_map(map_name, map_array):
    filename = map_name + ".json" # pega o nome do mapa e salva em .json, pra facilitar a leitura depois
    filepath = os.path.join(USER_MAP_PATH, filename)
    with open(filepath, "w") as f:
        json.dump(map_array, f)
        f.close()
    pygame.quit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor') # dá pra mudar mais tarde e rodar junto com o programa principal, talvez um main menu com escolha entre jogo e editor
clock = pygame.time.Clock()

renamebox = InputBox(100, 100, TILE_SIZE, TILE_SIZE) # posição tá zoada, precisa arrumar depois
working_map = load_map(os.path.join("assets", "maps","premade", "empty.json"))


waiting = True
while waiting:
    dialog_width = 500
    dialog_height = 300
    dialog_rect = pygame.Rect(
        (SCREEN_WIDTH - dialog_width) // 2,
        (SCREEN_HEIGHT - dialog_height) // 2,
        dialog_width,
        dialog_height
    )

    title_font = get_font(30)
    text_font = get_font(17)
    button_font = get_font(21)

    title_text = title_font.render("Criador de mapas", True, (255, 255, 255))

    controls_lines = [
        "Bem vindo ao criador de mapas!",
        "Clique na tela para mudar o objeto de cada quadrado",
        "",
        "Quando terminar, aperte S para digitar o nome do mapa",
        "Então aperte enter para salvar!",
    ]

    # Botão "Começar"
    start_btn = Buttons(
        pos=[dialog_rect.centerx, dialog_rect.bottom - 40],
        text_input="Começar!",
        font=button_font,
        base_color=(255, 255, 255),
        hover_color=(0, 255, 0)
    )


    draw_map(screen, working_map)
    # RETANGULO
    pygame.draw.rect(screen, (30, 30, 30), dialog_rect, border_radius=12)
    pygame.draw.rect(screen, (200, 200, 200), dialog_rect, 3, border_radius=12)
    # TITULO
    screen.blit(title_text, title_text.get_rect(center=(dialog_rect.centerx, dialog_rect.top + 30)))
    # TEXTO
    for i, line in enumerate(controls_lines):
        text = text_font.render(line, True, (255, 255, 255))
        screen.blit(text, (dialog_rect.left + 40, dialog_rect.top + 70 + i * 25))

    mouse_pos = pygame.mouse.get_pos()
    start_btn.check_for_input(mouse_pos)
    start_btn.change_color()
    start_btn.update(screen)

    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_btn.check_for_input(pygame.mouse.get_pos()):
                audio.play_sfx('menu_select')
                waiting = False
                running = True


while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if renamebox.active:
            mapname = renamebox.handle_event(event)
            if mapname:
                save_map(mapname, working_map) # salva o mapa

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
            if event.key == pygame.K_s: # aperta S pra abrir a caixa de texto
                if not renamebox.active:
                    renamebox.active = True

    draw_map(screen, working_map)
    if renamebox.active: # se ela estiver ativa, desenha na tela, depois do mapa pra ficar na frente
        renamebox.update()
        renamebox.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()