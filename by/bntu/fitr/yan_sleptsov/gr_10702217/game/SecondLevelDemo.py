import pygame,sys,math
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.Heroes as Heroes
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.Bumps as Bumps
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.SecondLevelData as Data2
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.FirstLevelData as Data1
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.Music as Music
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CaptionsAndMenu as CAndM
import by.bntu.fitr.yan_sleptsov.gr_10702217.game.CommonData as Data
def level2():
    done = True
    Music.mainSoundPlay(-1)
    Data.enemy.step = 1
    while done:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    if Data.hero.x > 0:
                        Data.hero.x -= 10
                if e.key == pygame.K_RIGHT:
                    if Data.hero.x < 800:
                        Data.hero.x += 10
                if e.key == pygame.K_UP:
                    if Data.hero.y > 350:
                        Data.hero.y -= 10
                if e.key == pygame.K_DOWN:
                    if Data.hero.y < 600:
                        Data.hero.y += 10
                if e.key == pygame.K_ESCAPE:
                    Data2.game.menu(Data.info_string,Data.screen,Data.window)
            if e.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                m = pygame.mouse.get_pos()
                if m[0] > 0 and m[0] < 800:
                    Data.hero.x = m[0]
                if m[1] > 350 and m[1] < 600:
                    Data.hero.y = m[1]
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    if Data.hero.push == False and Data2.arrowCounter > 0:
                        Music.pushSoundPlay(0)
                        Data.playerArrow.x = Data.hero.x
                        Data.playerArrow.y = Data.hero.y
                        Data.hero.push = True
                        Data2.arrowCounter -= 1
        Data.enemy.y = 20
        if Bumps.IntersectPlayer(Data.playerArrow.x, Data.enemy.x, Data.playerArrow.y, Data.enemy.y, 10, 35) == True:
            Data.enemyArrow.x = Data.enemy.x
            Data.enemyArrow.y = Data.enemy.y
            Data.enemy.push = True
        if Data.enemy.x > 0 and Data.enemy.x < 780:
            if Data.enemy.push == False:
                Data.enemyArrow.x = Data.enemy.x
                Data.enemyArrow.y = Data.enemy.y
                Data.enemy.push = True
        if Data.enemy.right == True:
            Data.enemy.x -= Data.enemy.step
            if Data.enemy.x < 0:
                Data2.score += 1
                Data.enemy.right = False
        else:
            Data.enemy.x += Data.enemy.step
            if Data.enemy.x > 780:
                Data2.score += 1
                Data.enemy.right = True
        if Data.playerArrow.y < 0:
            Data.hero.push = False
            Data2.score -= Data.enemy.step
        if Data.hero.push == False:
            Data.playerArrow.y = 700
            Data.playerArrow.x = -20
        else:
            Data.playerArrow.y -= 4
        if Data.enemyArrow.y > 800:
            Data.enemy.push = False
        if Data.enemy.push == False:
            Data.enemyArrow.y = -700
            Data.enemyArrow.x = 20
        else:
            Data.enemyArrow.y += 15
        if Bumps.IntersectPlayer(Data.playerArrow.x, Data.enemy.x, Data.playerArrow.y, Data.enemy.y, 10, 35) == True:
            Data.hero.push = False
            Data.enemy.step += 0.6
            Data2.score += Data.enemy.step
            Data.enemy.health -= 5
            Data.hero.health += 5
            Data2.arrowCounter += 2
        if Bumps.IntersectEnemy(Data.enemyArrow.x, Data.hero.x, Data.enemyArrow.y, Data.hero.y, 10, 35) == True:
            Data.enemy.push = False
            Data2.score -= 2
            Data.hero.health -= 5
            Data.enemy.health += 5
        Data.screen.blit(Data2.background_image, [0, 0])
        Data.info_string.fill((100, 0, 100))
        Data.playerArrow.render(Data.screen)
        Data.enemy.render(Data.screen)
        Data.hero.render(Data.screen)
        Data.enemyArrow.render(Data.screen)
        Data.info_string.blit(Data.speed_font.render(u'Speed: ' + str(round(Data.enemy.step, 2)), 1, (210, 120, 200)), (280, 5))
        Data.info_string.blit(Data.label_font.render(u'Blocks ' + str(Data2.arrowCounter), 1, (210, 120, 200)), (150, 5))
        Data.info_string.blit(Data.inf_font.render(u'Score: ' + str(round(Data2.score, 2)), 1, (0, 250, 200)), (2, 5))
        Data.info_string.blit(Data.hero_health_font.render(u'Hero health: ' + str(Data.hero.health), 1, (0, 250, 200)), (410, 5))
        Data.info_string.blit(Data.hero_health_font.render(u'Enemy health: ' + str(Data.enemy.health), 1, (0, 250, 200)), (600, 5))
        Data.window.blit(Data.info_string, (0, 0))
        Data.window.blit(Data.screen, (0, 30))
        pygame.display.flip()
        pygame.time.delay(1)
        print(Data.enemy.x)
        if Data.enemy.health <= 0 :
            print("Victory!!!")
            Music.main_sound.stop()
            Music.victorySoundPlay(0)
            end_puncts_win = [(220, 40, u'Congratulations!Victory! ', (250, 250, 30), (250, 30, 250), 0),
                              (250, 100, u'Your score is ' + str(round(Data2.score, 2)), (250, 250, 30), (250, 30, 250),1),
                              (250, 270, u'Go to the third level', (250, 250, 30), (250, 30, 250), 3),
                              (350, 320, u'Quit', (250, 250, 30), (250, 30, 250), 6)]
            end = CAndM.Caption(end_puncts_win)
            end.menu(Data.info_string,Data.screen,Data.window)
        elif Data2.score <= 0 or Data.hero.health <=0 or Data2.arrowCounter <= 0:
            Music.main_sound.stop()
            Music.lose_sound.play(0)

            end_puncts_lost = [(220, 40, u'You have lost!Try again! ', (250, 250, 30), (250, 30, 250), 0),
                               (250, 100, u'Your score is ' + str(round(Data2.score, 2)), (250, 250, 30), (250, 30, 250),1),
                               (250, 270, u'Try again this level', (250, 250, 30), (250, 30, 250), 4),
                               (350, 320, u'Quit', (250, 250, 30), (250, 30, 250), 6)]
            Data2.arrowCounter = Data1.arrowCounter
            Data2.score = Data1.score
            Data.enemy.step = 1
            Data.enemy.health = 100
            Data.hero.health = 100
            end = CAndM.Caption(end_puncts_lost)
            end.menu(Data.info_string,Data.screen,Data.window)
level2()
