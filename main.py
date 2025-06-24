import pygame, sys, os, json
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH
from src.buttons import Buttons
from src.audio import Audio
from main_game import run

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pybomber")
audio = Audio()
audio.play_sfx('game_open')
audio.play_music("assets/audio/music_1.mp3")

def get_font(size):
    return pygame.font.Font(FONT_PATH, size)

def get_maps():
    maps_dir = os.path.join(os.path.dirname(__file__), "./assets/maps")
    premade = []
    usermade = []
    for folder in ("premade", "usermade"):
        path = os.path.join(maps_dir, folder)
        for f in os.listdir(path):
            if f.endswith(".json"):
                premade.append({
                    "name": f.replace(".json", ""),
                    "path": os.path.join(path, f)
                }) if folder=="premade" else usermade.append({
                    "name": f.replace(".json", ""),
                    "path": os.path.join(path, f)
                })
    return premade + usermade

def load_map(path):
    with open(path, "r", encoding="utf-8") as fp:
        return json.load(fp)

def map_selection_menu():
    # Carregar a imagem de background
    background_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "./assets/images/background.png"))

    maps = get_maps()
    buttons = []
    for i, m in enumerate(maps):
        buttons.append(
            Buttons(
                pos=[SCREEN_WIDTH//2, SCREEN_HEIGHT//5 + 50*(i+1)],
                text_input=m["name"],
                font=get_font(20),
                base_color=(255,255,255),
                hover_color=(0,255,0)
            )
        )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        mouse_pos = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        title = get_font(50).render("Select a Map", True, (255,255,255))
        screen.blit(pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//10)))

        for btn, m in zip(buttons, maps):
            btn.check_for_input(mouse_pos)
            btn.change_color()
            if pygame.mouse.get_pressed()[0] and btn.check_for_input(mouse_pos):
                map_data = load_map(m["path"])
                print("Loaded map:", m["name"], map_data)
                return map_data

            btn.update(screen)

        pygame.display.update()

def main_menu():
    # Carregar a imagem de background
    background_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "./assets/images/background.png"))
    audio.play_random_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                if audio.volume_bar_rect_music.collidepoint(mouse_x, mouse_y):
                    audio.set_music_volume(mouse_x)
                if audio.mute_button_rect_music.collidepoint(mouse_x, mouse_y):
                    audio.mute_unmute_music()

                if audio.volume_bar_rect_sfx.collidepoint(mouse_x, mouse_y):
                    audio.set_sfx_volume(mouse_x)
                if audio.mute_button_rect_sfx.collidepoint(mouse_x, mouse_y):
                    audio.mute_unmute_sfx()

        mouse_pos = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        title = get_font(75).render("Pybomber", True, (255,255,255))
        screen.blit(pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//5)))

        audio.draw_music_hud(screen)
        audio.draw_sound_hud(screen)

        start_btn = Buttons(
            pos=[SCREEN_WIDTH//2, SCREEN_HEIGHT//2],
            text_input="Start",
            font=get_font(20),
            base_color=(255,255,255),
            hover_color=(0,255,0)
        )
        start_btn.check_for_input(mouse_pos)
        start_btn.change_color()
        if pygame.mouse.get_pressed()[0] and start_btn.check_for_input(mouse_pos):
            audio.play_sfx('menu_select')
            selected_map = map_selection_menu() # Não está aparecendo o controle de volume no menu de seleção de mapas, não consegui
            if selected_map:
                audio.play_sfx('game_start')
                run(selected_map, audio)
                audio.play_random_music()
                
        start_btn.update(screen)

        pygame.display.update()

if __name__ == '__main__':
    main_menu()

pygame.quit()
