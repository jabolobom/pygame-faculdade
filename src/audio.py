import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT


MUTE_BUTTON_WIDTH = SCREEN_WIDTH // 30
MUTE_BUTTON_HEIGHT = MUTE_BUTTON_WIDTH
BAR_WIDTH = SCREEN_WIDTH // 8
BAR_HEIGHT = MUTE_BUTTON_HEIGHT // 4
VOLUME_KNOB_RADIUS = (BAR_HEIGHT // 2) * 3
AUDIO_HUD_Y = SCREEN_HEIGHT - 35
TOTAL_AUDIO_HUD_WIDTH = BAR_WIDTH + 10 + MUTE_BUTTON_WIDTH


AUDIO_HUD_START_X = (SCREEN_WIDTH // 4) + 30 
MUSIC_MUTE_BUTTON_X = AUDIO_HUD_START_X
MUSIC_MUTE_BUTTON_Y = AUDIO_HUD_Y + (BAR_HEIGHT // 2) - (MUTE_BUTTON_HEIGHT // 2)
MUSIC_BAR_X = MUSIC_MUTE_BUTTON_X + MUTE_BUTTON_WIDTH + 10
MUSIC_BAR_Y = AUDIO_HUD_Y

MUSIC_HUD = {
    "BAR_WIDTH": BAR_WIDTH,
    "BAR_HEIGHT": BAR_HEIGHT,
    "MUTE_BUTTON_WIDTH": MUTE_BUTTON_WIDTH,
    "MUTE_BUTTON_HEIGHT": MUTE_BUTTON_HEIGHT,
    "MUSIC_BAR_X": MUSIC_BAR_X,
    "MUSIC_BAR_Y": MUSIC_BAR_Y,
    "MUSIC_MUTE_BUTTON_X": MUSIC_MUTE_BUTTON_X,
    "MUSIC_MUTE_BUTTON_Y": MUSIC_MUTE_BUTTON_Y,
    "VOLUME_KNOB_RADIUS": VOLUME_KNOB_RADIUS
}

SFX_HUD_START_X = MUSIC_BAR_X + BAR_WIDTH + 10 
VOLUME_MUTE_BUTTON_X = SFX_HUD_START_X
VOLUME_MUTE_BUTTON_Y = AUDIO_HUD_Y + (BAR_HEIGHT // 2) - (MUTE_BUTTON_HEIGHT // 2) 
VOLUME_BAR_X = VOLUME_MUTE_BUTTON_X + MUTE_BUTTON_WIDTH + 10
VOLUME_BAR_Y = AUDIO_HUD_Y 

VOLUME_HUD = {
    "BAR_WIDTH": BAR_WIDTH,
    "BAR_HEIGHT": BAR_HEIGHT,
    "MUTE_BUTTON_WIDTH": MUTE_BUTTON_WIDTH,
    "MUTE_BUTTON_HEIGHT": MUTE_BUTTON_HEIGHT,
    "VOLUME_BAR_X": VOLUME_BAR_X,
    "VOLUME_BAR_Y": VOLUME_BAR_Y,
    "VOLUME_MUTE_BUTTON_X": VOLUME_MUTE_BUTTON_X,
    "VOLUME_MUTE_BUTTON_Y": VOLUME_MUTE_BUTTON_Y,
    "VOLUME_KNOB_RADIUS": VOLUME_KNOB_RADIUS
}

class Audio:
    def __init__(self, source):
        pygame.mixer.music.load(source)
        self.current_volume_music = 0.5
        self.is_muted_music = False
        pygame.mixer.music.set_volume(self.current_volume_music)
        pygame.mixer.music.play(-1)

        self.music_note_img = pygame.image.load("assets/images/music_note.png").convert_alpha()
        self.music_note_img = pygame.transform.scale(self.music_note_img, (MUSIC_HUD['MUTE_BUTTON_WIDTH'], MUSIC_HUD['MUTE_BUTTON_HEIGHT']))

        self.volume_bar_rect_music = pygame.Rect(MUSIC_HUD['MUSIC_BAR_X'], MUSIC_HUD['MUSIC_BAR_Y'], MUSIC_HUD['BAR_WIDTH'], MUSIC_HUD['BAR_HEIGHT'])
        self.mute_button_rect_music = self.music_note_img.get_rect(topleft=(MUSIC_HUD['MUSIC_MUTE_BUTTON_X'], MUSIC_HUD['MUSIC_MUTE_BUTTON_Y']))


        self.current_volume_sfx = 0.5
        self.is_muted_sfx = False

        self.sfx_icon_img = pygame.image.load("assets/images/sound.png").convert_alpha()
        self.sfx_icon_img = pygame.transform.scale(self.sfx_icon_img, (VOLUME_HUD['MUTE_BUTTON_WIDTH'], VOLUME_HUD['MUTE_BUTTON_HEIGHT']))

        self.volume_bar_rect_sfx = pygame.Rect(VOLUME_HUD['VOLUME_BAR_X'], VOLUME_HUD['VOLUME_BAR_Y'], VOLUME_HUD['BAR_WIDTH'], VOLUME_HUD['BAR_HEIGHT'])
        self.mute_button_rect_sfx = self.sfx_icon_img.get_rect(topleft=(VOLUME_HUD['VOLUME_MUTE_BUTTON_X'], VOLUME_HUD['VOLUME_MUTE_BUTTON_Y']))

        self.sfx_sounds = {}
        self.load_sfx_sounds()

    def load_sfx_sounds(self):
        self.sfx_sounds['bomb_place'] = pygame.mixer.Sound("assets/audio/bomb_place.mp3")
        self.sfx_sounds['explosion'] = pygame.mixer.Sound("assets/audio/explosion.mp3")
        for sound in self.sfx_sounds.values():
            sound.set_volume(self.current_volume_sfx)

    def play_sfx(self, sfx_name):
        if not self.is_muted_sfx and sfx_name in self.sfx_sounds:
            self.sfx_sounds[sfx_name].set_volume(self.current_volume_sfx)
            self.sfx_sounds[sfx_name].play()

 

    def set_music_volume(self, mouse_x):
        new_volume_normalized = (mouse_x - MUSIC_HUD['MUSIC_BAR_X']) / MUSIC_HUD['BAR_WIDTH']
        self.current_volume_music = max(0.0, min(1.0, new_volume_normalized))
        pygame.mixer.music.set_volume(self.current_volume_music)
        if self.is_muted_music:
            self.is_muted_music = False

    def mute_unmute_music(self):
        if self.is_muted_music:
            self.is_muted_music = False
            pygame.mixer.music.set_volume(self.current_volume_music)
        else:
            self.is_muted_music = True
            pygame.mixer.music.set_volume(0)

    def draw_music_hud(self, screen):
        bar_rect = pygame.Rect(MUSIC_HUD['MUSIC_BAR_X'], MUSIC_HUD['MUSIC_BAR_Y'], MUSIC_HUD['BAR_WIDTH'], MUSIC_HUD['BAR_HEIGHT'])
        pygame.draw.rect(screen, (0, 0, 0), bar_rect, 0, border_radius=5)
        knob_x = MUSIC_HUD['MUSIC_BAR_X'] + int(self.current_volume_music * MUSIC_HUD['BAR_WIDTH'])
        knob_y = MUSIC_HUD['MUSIC_BAR_Y'] + (MUSIC_HUD['BAR_HEIGHT'] // 2)
        pygame.draw.circle(screen, (0, 0, 0), (knob_x, knob_y), MUSIC_HUD['VOLUME_KNOB_RADIUS'])

        screen.blit(self.music_note_img, (MUSIC_HUD['MUSIC_MUTE_BUTTON_X'], MUSIC_HUD['MUSIC_MUTE_BUTTON_Y']))

        if self.is_muted_music:
            bar_color = (255, 0, 0)
            start_pos = (MUSIC_HUD['MUSIC_MUTE_BUTTON_X'], MUSIC_HUD['MUSIC_MUTE_BUTTON_Y'] + MUSIC_HUD['MUTE_BUTTON_HEIGHT'])
            end_pos = (MUSIC_HUD['MUSIC_MUTE_BUTTON_X'] + MUSIC_HUD['MUTE_BUTTON_WIDTH'], MUSIC_HUD['MUSIC_MUTE_BUTTON_Y'])
            pygame.draw.line(screen, bar_color, start_pos, end_pos, 5)


    def set_sfx_volume(self, mouse_x):
        new_volume_normalized = (mouse_x - VOLUME_HUD['VOLUME_BAR_X']) / VOLUME_HUD['BAR_WIDTH']
        self.current_volume_sfx = max(0.0, min(1.0, new_volume_normalized))
        for sound in self.sfx_sounds.values():
            sound.set_volume(self.current_volume_sfx)
        if self.is_muted_sfx:
            self.is_muted_sfx = False

    def mute_unmute_sfx(self):
        if self.is_muted_sfx:
            self.is_muted_sfx = False
            for sound in self.sfx_sounds.values():
                sound.set_volume(self.current_volume_sfx)
        else:
            self.is_muted_sfx = True
            for sound in self.sfx_sounds.values():
                sound.set_volume(0)

    def draw_sound_hud(self, screen):
        bar_rect = pygame.Rect(VOLUME_HUD['VOLUME_BAR_X'], VOLUME_HUD['VOLUME_BAR_Y'], VOLUME_HUD['BAR_WIDTH'], VOLUME_HUD['BAR_HEIGHT'])
        pygame.draw.rect(screen, (0, 0, 0), bar_rect, 0, border_radius=5)

        knob_x = VOLUME_HUD['VOLUME_BAR_X'] + int(self.current_volume_sfx * VOLUME_HUD['BAR_WIDTH'])
        knob_y = VOLUME_HUD['VOLUME_BAR_Y'] + (VOLUME_HUD['BAR_HEIGHT'] // 2)
        pygame.draw.circle(screen, (0, 0, 0), (knob_x, knob_y), VOLUME_HUD['VOLUME_KNOB_RADIUS'])

        screen.blit(self.sfx_icon_img, (VOLUME_HUD['VOLUME_MUTE_BUTTON_X'], VOLUME_HUD['VOLUME_MUTE_BUTTON_Y']))

        if self.is_muted_sfx:
            bar_color = (255, 0, 0)
            start_pos = (VOLUME_HUD['VOLUME_MUTE_BUTTON_X'], VOLUME_HUD['VOLUME_MUTE_BUTTON_Y'] + VOLUME_HUD['MUTE_BUTTON_HEIGHT'])
            end_pos = (VOLUME_HUD['VOLUME_MUTE_BUTTON_X'] + VOLUME_HUD['MUTE_BUTTON_WIDTH'], VOLUME_HUD['VOLUME_MUTE_BUTTON_Y'])
            pygame.draw.line(screen, bar_color, start_pos, end_pos, 5)