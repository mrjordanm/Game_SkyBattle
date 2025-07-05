import pygame
import sys
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import C_RED, GAMEOVER_POS, C_YELLOW, WIN_WIDTH, WIN_HEIGHT


class GameOver:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/GameOverBg.png').convert_alpha()  # background
        self.rect = self.surf.get_rect(left=0, top=0)  # create rectangle
        pass

    def show(self):
        pygame.mixer_music.load('./asset/gameover.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.end_text(55,'GAME OVER! ;(', C_RED, GAMEOVER_POS['Title'])
            self.esc_text(14, 'RETURN (ESC)', C_YELLOW, (WIN_WIDTH - 70, WIN_HEIGHT - 10))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return  # return to menu

    # Fonts
    def end_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    # font ESC
    def esc_text (self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Verdana Bold", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)