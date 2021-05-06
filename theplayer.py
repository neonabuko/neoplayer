import pygame as pg
from pygame import mixer, image, display, transform
import time
pg.init()
mixer.init()
v = 1
p = i = t = c = 0
screen = display.set_mode((860, 710), vsync=1)
holy_img = transform.scale(image.load('megadeth.jpg'), (650, 550))
teger_img = transform.scale(image.load('tegernako.jpg'), (650, 550))
back = transform.scale(image.load('land.jpeg'), (850, 700))
imgs = [holy_img, teger_img]
pg.font.init()
helvetica45 = pg.font.SysFont("notomono", 45)
helvetica35 = pg.font.SysFont("notomono", 35)
helvetica30 = pg.font.SysFont("notomono", 30, italic=True)
helvetica25 = pg.font.SysFont("notomono", 25, italic=True)
helvetica20 = pg.font.SysFont("notomono", 20)
helvetica16 = pg.font.SysFont("notomono", 16)
helvetica20_italic = pg.font.SysFont("notomono", 20, italic=True)
titulo = helvetica45.render('{ NEO PLAYER }', True, (0, 0, 0))
opcao1 = helvetica25.render('1 - "Megadeth - Holy Wars"', True, (220, 220, 220))
opcao2 = helvetica25.render('2 - "Eluveitie - Tegernakô"', True, (220, 220, 220))
selecione = helvetica16.render('*Selecione a música pelo número', True, (200, 200, 200))
voltar = helvetica16.render('*Segure ESC para voltar ao menu', True, (200, 200, 200))
tithol = helvetica35.render('Megadeth - Holy Wars', True, (200, 200, 200))
titteg = helvetica35.render('Eluveitie - Tegernakô', True, (200, 200, 200))
author = helvetica20_italic.render('By $Neo', True, (180, 170, 160))
tits = [tithol, titteg]
display.set_caption('PLAYER')
som = mixer.Sound('holywars.ogg')
som2 = mixer.Sound('tegernako.ogg')
sons = [som, som2]
som.set_volume(v)
run = True
stop = False


def rel():
    s1 = s2 = m1 = m2 = p = 0
    s = v = 1
    menos = 0
    crun = True
    while crun:
        while 0 <= s1 <= 9:
            menos += 1
            tempo_restante = int(sons[i].get_length()) - menos
            print(tempo_restante)
            if tempo_restante < 0:
                crun = False
            screen.fill((20, 0, 0))
            screen.blit(imgs[i], (103, 40))
            screen.blit(tits[t], (103, 600))
            screen.blit(voltar, (58, 680))
            timer = helvetica20.render(f'{m2}{m1}:{s2}{s1}', True, (255, 255, 255))
            screen.blit(timer, (678, 600))
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    break
                key = pg.key.get_pressed()
                if event.type == pg.KEYDOWN:
                    if key[pg.K_ESCAPE]:
                        s = 0
                        print('Exiting...')
                        s1 = - 10
                        break
                    if p % 2 != 0:
                        if key[pg.K_SPACE]:
                            mixer.pause()
                            print('Pause')
                    else:
                        if key[pg.K_SPACE]:
                            mixer.unpause()
                            print('Resume')
                    p += 1
                    if key[pg.K_KP_PLUS]:
                        v += 0.1
                        if v > 1:
                            v = 1
                        sons[i].set_volume(v)
                        print(f'Volume {int(v * 100)}%')
                    if key[pg.K_KP_MINUS]:
                        v -= 0.1
                        if v < 0:
                            v = 0
                        sons[i].set_volume(v)
                        print(f'Volume {int(v * 100)}%')
                    if v > 1:
                        v = 1
                        print('Volume Max')
                    if v < 0:
                        v = 0
                        print('Volume Min')
            s1 += 1
            if 0 <= s1 <= 9:
                print(f'{m2}{m1}:{s2}{s1}')
                time.sleep(s)
        if s1 > - 8:
            s1 = 0
            s2 += 1
            if s2 == 6:
                s2 = 0
                m1 += 1
            if m1 == 10:
                m1 = 0
                m2 += 1
            print(f'{m2}{m1}:{s2}{s1}')
            time.sleep(s)
        else:
            crun = False
            sons[i].stop()
            p = 0


while run:
    busy = mixer.get_busy()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        key = pg.key.get_pressed()
        if event.type == pg.KEYDOWN:
            if key[pg.K_ESCAPE]:
                run = False
                print('Exiting...')
            if busy == 0:
                if key[pg.K_1] or key[pg.K_KP_1]:
                    som.play()
                    p = i = t = 0
                    print('Playing "Megadeth - Holy Wars"')
                    rel()
                if key[pg.K_2] or key[pg.K_KP_2]:
                    som2.play()
                    p = 0
                    t = i = 1
                    print('Playing "Eluveitie - Tegernakô"')
                    rel()
            else:
                if key[pg.K_1]:
                    som.stop()
                    som2.stop()
                    som.play()
                    p = 0
                    print('Playing "Megadeth - Holy Wars"')
                if key[pg.K_2]:
                    som2.stop()
                    som.stop()
                    som2.play()
                    p = 0
                    print('Playing "Eluveitie - Tegernakô"')
                if p % 2 != 0:
                    if key[pg.K_SPACE]:
                        mixer.pause()
                        print('Pause')
                else:
                    if key[pg.K_SPACE]:
                        mixer.unpause()
                        print('Resume')
            if key[pg.K_RETURN]:
                som.stop()
                som2.stop()
                stop = True
                print('Player stopped')
            if key[pg.K_KP_PLUS]:
                v += 0.1
                if v > 1:
                    v = 1
                som.set_volume(v)
                som2.set_volume(v)
                print(f'Volume {int(v * 100)}%')
            if key[pg.K_KP_MINUS]:
                v -= 0.1
                if v < 0:
                    v = 0
                som.set_volume(v)
                som2.set_volume(v)
                print(f'Volume {int(v * 100)}%')
            p += 1
            if v > 1:
                v = 1
                print('Volume Max')
            if v < 0:
                v = 0
                print('Volume Min')
            if stop:
                p = 0
                stop = False
    screen.fill((0, 10, 25))
    screen.blit(back, (5, 5))
    screen.blit(titulo, (250, 80))
    screen.blit(opcao1, (100, 450))
    screen.blit(opcao2, (100, 500))
    screen.blit(selecione, (50, 680))
    screen.blit(author, (750, 680))
    display.update()
