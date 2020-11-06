import pygame
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CaptionsAndMenu as Captions
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CommonData as Data
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.FirstLevelData as Data1

background_image = pygame.image.load("D:\sp3.jpg")
Data.screen.blit(background_image, [0, 0])

arrowCounter = Data1.arrowCounter
Data.enemy.health = 100
Data.hero.health = 100
score = Data1.score
Data.enemy.step = 1
punkts = [(300, 180, u'Play', (250, 250, 30), (250, 30, 250), 0),
          (300, 250, u'Quit', (250, 250, 30), (250, 30, 250), 1),
          (300, 10, u'Mario VS Enemy', (250, 250, 30), (250, 30, 250), 2),
          (350, 60, u'Level 2', (250, 250, 30), (250, 30, 250), 3)]
Data.hero.push = False
Data.enemy.push = False
game = Captions.Menu(punkts)
game.menu(Data.info_string, Data.screen, Data.window)
done = True
Data.enemy.right = False