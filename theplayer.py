#!/usr/bin/env python3

import pygame as pg
from pygame import mixer, image, display, transform
from pygame.locals import *
pg.init()
mixer.init()
screen = display.set_mode((860, 710), vsync=1)

# Images:

holy_img = transform.scale(image.load('./assets/megadeth.jpg'), (860, 710))
teger_img = transform.scale(image.load('./assets/tegernako.jpg'), (860, 710))
metallica_black_album = transform.scale(image.load('./assets/black_album.jpg'), (860, 710))
metallica_and_justice_for_all = transform.scale(image.load('./assets/and_justice_for_all.jpg'), (860, 710))
metallica_ride_the_lightning = transform.scale(image.load('./assets/ride_the_lightning.png'), (860, 710))
metallica_reload = transform.scale(image.load('./assets/reload.jpeg'), (860, 710))
back = transform.scale(image.load('./assets/land.jpeg'), (860, 710))
ball = transform.scale(image.load('./assets/circle.png'), (25, 25))
imgs = [holy_img, teger_img, metallica_reload, metallica_and_justice_for_all, metallica_black_album,
        metallica_black_album, metallica_black_album, metallica_ride_the_lightning, metallica_ride_the_lightning]
back.set_alpha(100)

# Fonts:

pg.font.init()
notomono45 = pg.font.SysFont("notomono", 45, bold=True)
notomono35 = pg.font.SysFont("notomono", 35)
notomono30 = pg.font.SysFont("notomono", 30, italic=True)
notomono25 = pg.font.SysFont("notomono", 25)
notomono20 = pg.font.SysFont("notomono", 20)
notomono16 = pg.font.SysFont("notomono", 16)
notomono20_italic = pg.font.SysFont("notomono", 20, italic=True)
player = notomono45.render('{ NEO PLAYER }', True, (255, 255, 255))

# Menu:

display.set_caption('NEO PLAYER')
opt1 = notomono25.render('1 - Megadeth  - Holy Wars', True, (250, 250, 250))
opt2 = notomono25.render('2 - Eluveitie - Tegernakô', True, (250, 250, 250))
opt3 = notomono25.render('3 - Metallica - Fuel', True, (250, 250, 250))
opt4 = notomono25.render('4 - Metallica - One', True, (250, 250, 250))
opt5 = notomono25.render('5 - Metallica - Enter Sandman', True, (250, 250, 250))
opt6 = notomono25.render('6 - Metallica - The Unforgiven', True, (250, 250, 250))
opt7 = notomono25.render('7 - Metallica - Nothing Else Matters', True, (250, 250, 250))
opt8 = notomono25.render('8 - Metallica - Fade to Black', True, (250, 250, 250))
opt9 = notomono25.render('9 - Metallica - For Whom the Bell Tolls', True, (250, 250, 250))
options = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9]
selecione = notomono16.render('*Selecione a música pelo número', True, (200, 200, 200))
author = notomono20_italic.render('By $Neo', True, (180, 170, 160))

# Music screen:

play = pg.transform.scale(pg.image.load('./assets/play.png'), (35, 35))
pause = pg.transform.scale(pg.image.load('./assets/pause.png'), (35, 35))
play_pause = [play, pause]

# Songs:

som = mixer.Sound('./assets/holywars.ogg')
loading_text = notomono25.render('Loaded "Holy Wars"', True, (250, 250, 250))
screen.blit(loading_text, (180, 100))
display.update()
som2 = mixer.Sound('./assets/tegernako.ogg')
loading_text = notomono25.render('Loaded "Tegernakô"', True, (250, 250, 250))
screen.blit(loading_text, (180, 150))
display.update()
som3 = mixer.Sound('./assets/Metallica - Fuel (Official Music Video).ogg')
loading_text = notomono25.render('Loaded "Fuel"', True, (250, 250, 250))
screen.blit(loading_text, (180, 200))
display.update()
som4 = mixer.Sound('./assets/Metallica: One (Official Music Video).ogg')
loading_text = notomono25.render('Loaded "One"', True, (250, 250, 250))
screen.blit(loading_text, (180, 250))
display.update()
som5 = mixer.Sound('./assets/Metallica: Enter Sandman (Official Music Video).ogg')
loading_text = notomono25.render('Loaded "Enter Sandman"', True, (250, 250, 250))
screen.blit(loading_text, (180, 300))
display.update()
som6 = mixer.Sound('./assets/Metallica - The Unforgiven (Official Music Video).ogg')
loading_text = notomono25.render('Loaded "The Unforgiven"', True, (250, 250, 250))
screen.blit(loading_text, (180, 350))
display.update()
som7 = mixer.Sound('./assets/Metallica: Nothing Else Matters (Official Music Video).ogg')
loading_text = notomono25.render('Loaded "Nothing Else Matters"', True, (250, 250, 250))
screen.blit(loading_text, (180, 400))
display.update()
som8 = mixer.Sound('./assets/Fade To Black.ogg')
loading_text = notomono25.render('Loaded "Fade to Black"', True, (250, 250, 250))
screen.blit(loading_text, (180, 450))
display.update()
som9 = mixer.Sound('./assets/For Whom The Bell Tolls.ogg')
loading_text = notomono25.render('Loaded "For Whom The Bell Tolls"', True, (250, 250, 250))
screen.blit(loading_text, (180, 500))
display.update()
sons = [som, som2, som3, som4, som5, som6, som7, som8, som9]


def playing(i):
    v = 1
    p2 = 0
    pp = 1
    color_change = 0
    z = 3
    img_movement = 1200
    playrun = True
    pr = 125
    clock = pg.time.Clock()
    while playrun:
        busy1 = mixer.get_busy()
        for event1 in pg.event.get():
            if event1.type == pg.QUIT:
                playrun = False
            if event1.type == KEYDOWN:
                key1 = pg.key.get_pressed()
                if key1[pg.K_ESCAPE]:
                    z = - 3
                    sons[i].stop()
                    playrun = False
                    print('Exiting...')
                if busy1 == 0:
                    if key1[pg.K_1]:
                        i = 0
                        sons[i].stop()
                        sons[i].play()
                        print('Playing "Megadeth - Holy Wars"')
                    if key1[pg.K_2]:
                        som2.stop()
                        som.stop()
                        som2.play()
                        p2 = 0
                        print('Playing "Eluveitie - Tegernakô"')
                if p2 % 2 == 0:
                    if key1[pg.K_SPACE]:
                        mixer.pause()
                        p2 += 1
                        pp = 0
                        print('Pause')
                else:
                    if key1[pg.K_SPACE]:
                        mixer.unpause()
                        p2 += 1
                        pp = 1
                        print('Resume')
                if key1[pg.K_KP_PLUS]:
                    v += 0.1
                    if v > 1:
                        v = 1
                    sons[i].set_volume(v)
                    print(f'Volume {int(v * 100)}%')
                    if v >= 1:
                        v = 1
                        print('Volume Max')
                if key1[pg.K_KP_MINUS]:
                    v -= 0.1
                    if v < 0:
                        v = 0
                    sons[i].set_volume(v)
                    print(f'Volume {int(v * 100)}%')
                    if v <= 0:
                        v = 0
                        print('Volume Min')
        clock.tick(100)
        s = sons[i].get_length()
        d = 6 / s
        pr += d
        img_movement -= 30
        if img_movement < 0:
            img_movement = 0
        if img_movement < 1:
            color_change += z
        if color_change > 220:
            color_change = 220
        if color_change < 0:
            color_change = 0
        if p2 % 2 != 0:
            pr -= d
        if pr > 690:
            pr = 690
        rect1_size = (860, 160)
        transp = pg.Surface(rect1_size, pg.SRCALPHA)
        voltar = notomono16.render('* ESC = Menu', True, (color_change, color_change, color_change))
        tithol = notomono35.render('Megadeth - Holy Wars', True, (255, 255, 255))
        titteg = notomono35.render('Eluveitie - Tegernakô', True, (255, 255, 255))
        fuel = notomono35.render('Metallica - Fuel', True, (255, 255, 255))
        one = notomono35.render('Metallica - One', True, (255, 255, 255))
        entersandman = notomono35.render('Metallica - Enter Sandman', True, (255, 255, 255))
        theunforgiven = notomono35.render('Metallica - The Unforgiven', True, (255, 255, 255))
        nothingelsematters = notomono35.render('Metallica - Nothing Else Matters', True, (255, 255, 255))
        fadetoblack = notomono35.render('Metallica - Fade to Black', True, (255, 255, 255))
        forwhomthebelltolls = notomono35.render('Metallica - For Whom the Bell Tolls', True, (255, 255, 255))
        tits = [tithol, titteg, fuel, one, entersandman, theunforgiven, nothingelsematters, fadetoblack,
                forwhomthebelltolls]
        volume = notomono20.render(f'Volume {int(v * 100)}%', True, (color_change, color_change, color_change))
        branco = (color_change, color_change, color_change)
        preto_transp = (0, 0, 0, color_change)
        pg.draw.rect(transp, preto_transp, transp.get_rect(), 500)
        screen.fill((0, 0, 0))
        screen.blit(imgs[i], (img_movement, 0))
        imgs[i].set_alpha(color_change * 10)
        screen.blit(transp, (0, 550))
        pg.draw.rect(screen, (0, 0, 0), (84, 577, tits[i].get_width() + 40, 50), border_radius=3)
        screen.blit(tits[i], (103, 580))
        screen.blit(voltar, (600, 688))
        pg.draw.rect(screen, branco, (120, 661, 633, 2), border_radius=20)
        pg.draw.circle(screen, branco, center=(pr + 10, 662), radius=11)
        screen.blit(volume, (620, 620))
        pg.draw.rect(screen, branco, (72, 643, 38, 38), border_radius=20)
        screen.blit(play_pause[pp], (73, 644))
        pg.display.update()


nivel_transp = 255
button_number = 0
y = 295
yt = 290
i = 0
t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
run = True
while run:
    mouse = pg.mouse.get_pressed(num_buttons=5)
    mx, my = pg.mouse.get_pos()
    if 30 < mx < 830:
        if 292 < my < 328:
            t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t0 = 255
        elif 330 < my < 368:
            t0 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t1 = 255
        elif 370 < my < 408:
            t0 = t1 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t2 = 255
        elif 410 < my < 448:
            t0 = t1 = t2 = t4 = t5 = t6 = t7 = t8 = 60
            t3 = 255
        elif 450 < my < 488:
            t0 = t1 = t2 = t3 = t5 = t6 = t7 = t8 = 60
            t4 = 255
        elif 490 < my < 528:
            t0 = t1 = t2 = t3 = t4 = t6 = t7 = t8 = 60
            t5 = 255
        elif 530 < my < 568:
            t0 = t1 = t2 = t3 = t4 = t5 = t7 = t8 = 60
            t6 = 255
        elif 570 < my < 608:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t8 = 60
            t7 = 255
        elif 610 < my < 648:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = 60
            t8 = 255
        else:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
    else:
        t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
    busy = mixer.get_busy()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        key = pg.key.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            button_number = event.button
            if button_number == 1:
                if 30 < mx < 830:
                    if 292 < my < 328:
                        p = i = t = 0
                        sons[i].play()
                        playing(i)
                    if 330 < my < 368:
                        p = i = t = 1
                        sons[i].play()
                        playing(i)
                    if 370 < my < 408:
                        p = i = t = 2
                        sons[i].play()
                        playing(i)
                    if 410 < my < 448:
                        p = i = t = 3
                        sons[i].play()
                        playing(i)
                    if 450 < my < 488:
                        p = i = t = 4
                        sons[i].play()
                        playing(i)
                    if 490 < my < 528:
                        p = i = t = 5
                        sons[i].play()
                        playing(i)
                    if 530 < my < 578:
                        p = i = t = 6
                        sons[i].play()
                        playing(i)
                    if 580 < my < 618:
                        p = i = t = 7
                        sons[i].play()
                        playing(i)
                    if 620 < my < 658:
                        p = i = t = 8
                        sons[i].play()
                        playing(i)
        if event.type == pg.KEYDOWN:
            if key[pg.K_ESCAPE]:
                run = False
                print('Exiting...')
            if busy == 0:
                if key[pg.K_1] or key[pg.K_KP_1]:
                    p = i = t = 0
                    sons[i].play()
                    print('Playing "Megadeth - Holy Wars"')
                    playing(i)
                if key[pg.K_2] or key[pg.K_KP_2]:
                    p = 0
                    t = i = 1
                    som2.play()
                    print('Playing "Eluveitie - Tegernakô"')
                    playing(i)
    screen.fill((0, 0, 10))
    screen.blit(back, (0, 0))
    screen.blit(player, (210, 80))
    rect_size = (840, 40)
    transp0 = pg.Surface(rect_size, pg.SRCALPHA)
    transp1 = pg.Surface(rect_size, pg.SRCALPHA)
    transp2 = pg.Surface(rect_size, pg.SRCALPHA)
    transp3 = pg.Surface(rect_size, pg.SRCALPHA)
    transp4 = pg.Surface(rect_size, pg.SRCALPHA)
    transp5 = pg.Surface(rect_size, pg.SRCALPHA)
    transp6 = pg.Surface(rect_size, pg.SRCALPHA)
    transp7 = pg.Surface(rect_size, pg.SRCALPHA)
    transp8 = pg.Surface(rect_size, pg.SRCALPHA)
    transp = [transp0, transp1, transp2, transp3, transp4, transp5, transp6, transp7, transp8]
    pg.draw.rect(transp0, (0, 30, 120, t0), transp0.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp1, (0, 30, 120, t1), transp1.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp2, (0, 30, 120, t2), transp2.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp3, (0, 30, 120, t3), transp3.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp4, (0, 30, 120, t4), transp4.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp5, (0, 30, 120, t5), transp5.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp6, (0, 30, 120, t6), transp6.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp7, (0, 30, 120, t7), transp7.get_rect(), 20, border_radius=50)
    pg.draw.rect(transp8, (0, 30, 120, t8), transp8.get_rect(), 20, border_radius=50)
    for k in range(0, len(transp)):
        screen.blit(transp[k], (10, yt + (k * 42)))
    for k in range(0, len(options)):
        screen.blit(options[k], (30, y + (k * 42)))
    screen.blit(selecione, (50, 680))
    screen.blit(author, (750, 680))
    display.update()
