import pygame, sys
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.Music as Music

background_image = pygame.image.load("D:\menu.jpg")


class Menu:
    def __init__(self, punkts=[120, 140, u'Punct', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, info_string, screen, window):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(background_image, [0, 0])
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.puncts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
                    elif punkt == 2:
                        pass
                    elif punkt == 3:
                        pass
            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))

            pygame.display.flip()


class Caption:
    def __init__(self, punkts=[120, 140, u'Punct', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, surface, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self, info_string, screen, window):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.blit(background_image, [0, 0])
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 310 and mp[1] > i[1] and mp[1] < i[1] + 100:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.puncts) - 1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        pass
                    elif punkt == 1:
                        pass
                    elif punkt == 2:
                        import by.bntu.fitr.yan_sleptsov.gr_10702217.game.SecondLevel
                        Music.mainSoundPlay(-1)
                    elif punkt == 3:
                        import by.bntu.fitr.yan_sleptsov.gr_10702217.game.ThirdLevel
                        Music.mainSoundPlay(-1)
                    elif punkt == 4:
                        Music.mainSoundPlay(-1)
                        done = False
                    elif punkt == 5:
                        import by.bntu.fitr.yan_sleptsov.gr_10702217.game.FirstLevel
                        Music.mainSoundPlay(-1)
                    elif punkt == 6:
                        sys.exit()
            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()