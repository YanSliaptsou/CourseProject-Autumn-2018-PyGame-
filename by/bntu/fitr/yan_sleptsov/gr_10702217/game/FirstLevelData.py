import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CaptionsAndMenu as Captions
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CommonData as Data
import pygame

background_image = pygame.image.load("D:\space.jpg")
Data.screen.blit(background_image, [0, 0])

arrowCounter = 500
score = 1000
Data.enemy.health = 100
Data.hero.health = 100
punkts = [(300, 180, u'Play', (250, 250, 30), (250, 30, 250), 0),
          (300, 250, u'Quit', (250, 250, 30), (250, 30, 250), 1),
          (300, 10, u'Mario VS Enemy', (250, 250, 30), (250, 30, 250), 2),
          (350, 60, u'Level 1', (250, 250, 30), (250, 30, 250), 3)]
Data.hero.push = False
Data.enemy.push = False
game = Captions.Menu(punkts)
game.menu(Data.info_string, Data.screen, Data.window)
done = True
Data.enemy.right = False