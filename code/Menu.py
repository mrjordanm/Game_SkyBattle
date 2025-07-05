import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION, C_BLUE2, C_BLUE1, C_BLUE3

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha() # background
        self.rect = self.surf.get_rect(left=0, top=0) # create rectangle

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu.wav') # load music
        pygame.mixer_music.play(-1) # loop

        while True:
            self.window.blit(source=self.surf, dest=self.rect) # DRAW IMAGES
            self.menu_text(50, "Sky", C_BLUE1, ((WIN_WIDTH / 2), 70))
            self.menu_text(55, "Battle", C_BLUE2, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_BLUE3, ((WIN_WIDTH / 2), 180 + 25 * i))
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 177 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 180 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # close Window
                    quit() # end pygame
                if event.type == pygame.KEYDOWN:
                    # select sound
                    sect = pygame.mixer.Sound('./asset/select.wav')
                    sect.set_volume(0.2)
                    sect.play()
                    if event.key == pygame.K_DOWN: # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    # fonts
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)