import pygame


class Buttons():
    def __init__(self, pos, text_input, font, base_color, hover_color):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, base_color)
        self.base_color, self.hover_color = base_color, hover_color
        self.active = False

        self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.text, self.rect)

    def change_color(self):
        if self.active:
            self.text = self.font.render(self.text_input, True, self.hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def check_for_input(self, position):
        if self.rect.collidepoint(position):
            self.active = True
            return True
        else:
            self.active = False
            return False
