import pygame
from src.settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BG_COLOR = pygame.Color("darkblue")
FONT = pygame.font.SysFont("comicsans", 32)

class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BG_COLOR
        self.text = text
        self.txt_surface = FONT.render(self.text, False, BG_COLOR)
        self.active = False

    def handle_event(self, event):
            if self.active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        outputname = self.text
                        self.text = ''
                        self.active = False
                        return outputname
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode

                    self.txt_surface = FONT.render(self.text, False, BG_COLOR)
            return 0
    def update(self):
        width = max(200, self.txt_surface.get_width()+10) # +10 = margem
        self.rect.width = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


