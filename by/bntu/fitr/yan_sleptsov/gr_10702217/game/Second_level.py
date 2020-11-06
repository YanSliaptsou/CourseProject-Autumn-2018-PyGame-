import pygame,math,sys
from pygame import mixer
class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
def Intersect(x1,x2,y1,y2,db1,db2):
    if(x1>x2-db1) and (x1<x2+db2) and (y1>y2-db1) and (y1<y2+db2):
        return 1
    else:
        return 0
class Menu:
    def __init__(self,punkts=[120,140,u'Punct',(250,250,30),(250,30,250)]):
        self.punkts= punkts
    def render(self,poverhnost,font,num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2],1,i[4]),(i[0],i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self,enumerator):
        done=True
        font_menu = pygame.font.Font(None,50)
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            info_string.fill((0,100,200))
            screen.fill((0,100,200))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen,font_menu,punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt-=1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.puncts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done =False
                    elif punkt == 1:
                        sys.exit()
            window.blit(info_string,(0,0))
            window.blit(screen,(0,30))
            pygame.display.flip()
window=pygame.display.set_mode((400,430))
pygame.display.set_caption("It is my first game Python")
screen=pygame.Surface((400,400))
info_string=pygame.Surface((400,30))
pygame.font.init()
speed_font = pygame.font.Font(None,32)
inf_font = pygame.font.SysFont(None,32)
label_font = pygame.font.SysFont(None,32)
hero=Sprite(350,350,'D:\mar.png')
zet=Sprite(10,10,'D:\j.png')
zet.right = False
zet.step = 1.0
strela=Sprite(-10,350,'D:\pl.png')
strela.push = False
arrow=30
enumerator = 10
punkts = [(120,140,u'Game',(250,250,30),(250,30,250),0),
          (130,210,u'Quit',(250,250,30),(250,30,250),1)]
game = Menu(punkts)
game.menu(enumerator)
done=True
pygame.key.set_repeat(1,1)
pygame.mixer.pre_init(44100,-16,1,512)
pygame.mixer.init()
main_sound = pygame.mixer.Sound('D:\main.ogg')
push_sound = pygame.mixer.Sound('D:\push.ogg')
win_sound = pygame.mixer.Sound('D:\end.ogg')
main_sound.play(-1)
def main():
    window = pygame.display.set_mode((400, 430))
    pygame.display.set_caption("It is my first game Python")
    screen = pygame.Surface((400, 400))
    info_string = pygame.Surface((400, 30))
    pygame.font.init()
    speed_font = pygame.font.Font(None, 32)
    inf_font = pygame.font.SysFont(None, 32)
    label_font = pygame.font.SysFont(None, 32)
    hero = Sprite(350, 350, 'D:\mar.png')
    zet = Sprite(10, 10, 'D:\j.png')
    zet.right = False
    zet.step = 1.0
    strela = Sprite(-10, 350, 'D:\pl.png')
    strela.push = False
    arrow = 30
    enumerator = 10
    punkts = [(120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0),
              (130, 210, u'Quit', (250, 250, 30), (250, 30, 250), 1)]
    game = Menu(punkts)
    game.menu(enumerator)
    done = True
    pygame.key.set_repeat(1, 1)
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.mixer.init()
    main_sound = pygame.mixer.Sound('D:\main.ogg')
    push_sound = pygame.mixer.Sound('D:\push.ogg')
    win_sound = pygame.mixer.Sound('D:\end.ogg')
    main_sound.play(-1)
    while done:
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                done=False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    if hero.x > 10:
                        hero.x -=1
                if e.key == pygame.K_RIGHT:
                    if hero.x < 350:
                        hero.x +=1
                if e.key == pygame.K_UP:
                    if hero.y > 275:
                        hero.y -= 1
                if e.key == pygame.K_DOWN:
                    if hero.y < 350:
                        hero.y += 1
                if e.key == pygame.K_ESCAPE:
                    game.menu(enumerator)
            if e.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                m = pygame.mouse.get_pos()
                if m[0] > 10 and m[0] < 350:
                    hero.x = m[0]
                if m[1] > 275 and m[1] < 350:
                    hero.y = m[1]
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    hero = Sprite(hero.x, hero.y, 'D:\d.png')
                    push_sound.play(0)
                    if strela.push == False:
                        strela.x = hero.x
                        strela.y = hero.y
                        strela.push = True
                        arrow-=1
        screen.fill((50,50,50))
        info_string.fill((45,80,40))
        if zet.right == True:
            zet.x -= zet.step
            if zet.x < 0:
                zet.right = False
        else:
            zet.x += zet.step
            if zet.x > 350:
                zet.right = True
        if strela.y < 0:
            hero = Sprite(hero.x, hero.y, 'D:\mar.png')
            strela.push = False
            enumerator -=  math.fmod(zet.step,10)
        if strela.push == False:
            strela.y = 350
            strela.x = -10
        else:
            strela.y -= 2
        if Intersect(strela.x,zet.x,strela.y,zet.y,5,40)== True:
            hero = Sprite(hero.x, hero.y, 'D:\mar.png')
            strela.push = False
            zet.step += 0.3
            enumerator += math.fmod(zet.step,10)
        strela.render()
        zet.render()
        hero.render()
        info_string.blit(speed_font.render(u'Speed: '+str(round(zet.step,2)),1,(210,120,200)),(260,5))
        info_string.blit(label_font.render(u'Blocks ' +str(arrow),1,(210,120,200)),(140,5))
        info_string.blit(inf_font.render(u'Score: '+str(round(enumerator,2)),1,(0,250,200)),(2,5))
        window.blit(info_string,(0,0))
        window.blit(screen, (0, 30))
        pygame.display.flip()
        pygame.time.delay(5)
        if arrow<0 :
            main_sound.stop()
            win_sound.play(-1)
            end_puncts_win = [(0, 140, u'Congratulations!Victory! ', (250, 250, 30), (250, 30, 250), 0),
                      (70, 210, u'Your score is ' + str(round(enumerator, 2)), (250, 250, 30), (250, 30, 250), 1)]
            end = Menu(end_puncts_win)
            end.menu(enumerator)
        elif enumerator < 0:
            main_sound.stop()
            win_sound.play(-1)
            end_puncts_lost = [(5, 140, u'You have lost!Try again! ', (250, 250, 30), (250, 30, 250), 0),
                      (70, 210, u'Your score is ' + str(round(enumerator, 2)), (250, 250, 30), (250, 30, 250), 1)]
            end = Menu(end_puncts_lost)
            end.menu(enumerator)
