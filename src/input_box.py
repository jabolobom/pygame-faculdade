import pygame
from src.settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def get_font(size):
    return pygame.font.Font(FONT_PATH, size)

BG_COLOR = pygame.Color("darkblue")
FONT_COLOR = pygame.Color("white")
FONT = get_font(32)

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BG_COLOR
        self.text = text
        self.txt_surface = FONT.render(self.text, False, FONT_COLOR)
        self.active = False

    def handle_event(self, event):
            if self.active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: # se apertar enter
                        self.active = False
                        return self.text # retorna o texto escrito
                    elif event.key == pygame.K_BACKSPACE: # apagar texto
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

                    self.txt_surface = FONT.render(self.text, False, FONT_COLOR)
            return 0

    def update(self): # atualiza a aparencia, aumenta conforme o texto
        width = max(200, self.txt_surface.get_width()+10) # +10 = margem
        self.rect.width = width

    def draw(self, screen): #
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))



