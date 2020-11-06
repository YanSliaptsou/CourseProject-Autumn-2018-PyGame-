import pygame


class Player:
    def __init__(self, xpos, ypos, filename, health):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
        self.health = health

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))

    def push(self):
        pass


class Enemy:
    def __init__(self, xpos, ypos, filename, health, step=1):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
        self.health = health
        self.step = step

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))


class Arrow:
    def __init__(self, xpos, ypos, filename, health):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0, 0, 0))
        self.health = health

    def render(self, screen):
        screen.blit(self.bitmap, (self.x, self.y))