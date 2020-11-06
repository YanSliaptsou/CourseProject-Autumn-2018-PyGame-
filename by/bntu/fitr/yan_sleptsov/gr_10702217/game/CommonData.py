import pygame
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.Heroes as Heroes

screen = pygame.Surface((800, 600))
window = pygame.display.set_mode((800, 630))
pygame.display.set_caption("Mario VS Enemy")
info_string = pygame.Surface((800, 40))
pygame.font.init()
speed_font = pygame.font.Font(None, 32)
inf_font = pygame.font.SysFont(None, 32)
label_font = pygame.font.SysFont(None, 32)
hero_health_font = pygame.font.SysFont(None, 32)
enemy_health_font = pygame.font.SysFont(None, 32)
hero = Heroes.Player(350, 350, 'D:\mar.png', 50)
enemy = Heroes.Enemy(50, 50, 'D:\j.png', 100)
enemy2 = Heroes.Enemy(50, 50, 'D:\j.png', 100)
playerArrow = Heroes.Arrow(-10, 350, 'D:\pl.png', 0)
enemyArrow = Heroes.Arrow(-10, 350, 'D:\pl.png',0)
enemy2Arrow = Heroes.Arrow(-10, 350, 'D:\pl.png',0)