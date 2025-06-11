import pygame, sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_PATH
from src.buttons import Buttons

# arquivo de telas do menu principal, futuramente irá controlar quando o jogo inicia/troca de fase, etc.

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pybomber")

background = None # carregar uma imagem, um padrão repetido pra ficar parecido com os main menu da era do NES ficaria legal

def get_font(size): # redimensiona a fonte conforme necessário
    return pygame.font.Font(FONT_PATH, size)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((0, 0, 0))

        title = get_font(75).render("Pybomber", True, (255, 255, 255))
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))

        startgame_button = Buttons(pos=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], text_input='Start', font=get_font(20), base_color=(255,255,255), hover_color=(0,255,0))
        startgame_button.update(screen)

        screen.blit(title, title_rect)
        pygame.display.update()

main_menu()
pygame.quit()