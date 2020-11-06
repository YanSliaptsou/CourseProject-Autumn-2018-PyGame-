import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
main_sound = pygame.mixer.Sound('D:\main.ogg')
push_sound = pygame.mixer.Sound('D:\push.ogg')
win_sound = pygame.mixer.Sound('D:\end.ogg')
lose_sound = pygame.mixer.Sound('D:\lose.ogg')


def mainSoundPlay(fr):
    main_sound.play(fr)


def victorySoundPlay(fr):
    win_sound.play(fr)


def pushSoundPlay(fr):
    push_sound.play(fr)


def loseSoundPlay(fr):
    lose_sound.play(fr)