import pygame
from src.settings import VOLUME_HUD

class Audio:
    def __init__(self, source):
        pygame.mixer.init()
        pygame.mixer.music.load(source)
        self.current_volume = 0.5
        self.is_muted = False
        pygame.mixer.music.set_volume(self.current_volume)
        pygame.mixer.music.play(-1)

        self.music_note_img = pygame.image.load("assets/images/music_note.png").convert_alpha()
        self.music_note_img = pygame.transform.scale(self.music_note_img, (VOLUME_HUD['MUTE_BUTTON_WIDTH'], VOLUME_HUD['MUTE_BUTTON_HEIGHT']))
        self.volume_bar_rect = pygame.Rect(VOLUME_HUD['VOLUME_BAR_X'], VOLUME_HUD['VOLUME_BAR_Y'], VOLUME_HUD['VOLUME_BAR_WIDTH'], VOLUME_HUD['VOLUME_BAR_HEIGHT'])

        self.mute_button_rect = self.music_note_img.get_rect(topleft=(VOLUME_HUD['MUTE_BUTTON_X'], VOLUME_HUD['MUTE_BUTTON_Y']))

 

    def set_volume(self, mouse_x):
        new_volume_normalized = (mouse_x - VOLUME_HUD['VOLUME_BAR_X']) / VOLUME_HUD['VOLUME_BAR_WIDTH']
        self.current_volume = max(0.0, min(1.0, new_volume_normalized))
        pygame.mixer.music.set_volume(self.current_volume)
        if self.is_muted:
            self.is_muted = False
    
    def mute_unmute(self):
        if self.is_muted:
            self.is_muted = False
            pygame.mixer.music.set_volume(self.current_volume)
        else:
            self.is_muted = True
            pygame.mixer.music.set_volume(0)

    def draw_volume_bar(self, screen):
        bar_rect = pygame.Rect(VOLUME_HUD['VOLUME_BAR_X'], VOLUME_HUD['VOLUME_BAR_Y'], VOLUME_HUD['VOLUME_BAR_WIDTH'], VOLUME_HUD['VOLUME_BAR_HEIGHT'])
        pygame.draw.rect(screen, (0, 0, 0), bar_rect, 0, border_radius=5)
        knob_x = VOLUME_HUD['VOLUME_BAR_X'] + int(self.current_volume * VOLUME_HUD['VOLUME_BAR_WIDTH'])
        knob_y = VOLUME_HUD['VOLUME_BAR_Y'] + (VOLUME_HUD['VOLUME_BAR_HEIGHT'] // 2)
        pygame.draw.circle(screen, (0, 0, 0), (knob_x, knob_y), VOLUME_HUD['VOLUME_KNOB_RADIUS'])

    def draw_mute_button(self, screen):
        screen.blit(self.music_note_img, (VOLUME_HUD['MUTE_BUTTON_X'], VOLUME_HUD['MUTE_BUTTON_Y']))

        if self.is_muted:
            bar_color = (255, 0, 0)
            start_pos = (VOLUME_HUD['MUTE_BUTTON_X'], VOLUME_HUD['MUTE_BUTTON_Y'] + VOLUME_HUD['MUTE_BUTTON_HEIGHT'])
            end_pos = (VOLUME_HUD['MUTE_BUTTON_X'] + VOLUME_HUD['MUTE_BUTTON_WIDTH'], VOLUME_HUD['MUTE_BUTTON_Y'])
            pygame.draw.line(screen, bar_color, start_pos, end_pos, 5)
            
                
