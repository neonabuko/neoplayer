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
quicksand60 = pg.font.SysFont("quicksand", 60)
notomono35 = pg.font.SysFont("notomono", 35)
notomono30_italic = pg.font.SysFont("notomono", 30, italic=True)
quicksand38 = pg.font.SysFont("quicksand", 38)
quicksand22 = pg.font.SysFont("quicksand", 22)
notomono22 = pg.font.SysFont("notomono", 22)
quicksand20 = pg.font.SysFont("quicksand", 20)
notomono16 = pg.font.SysFont("notomono", 16)
notomono20_italic = pg.font.SysFont("notomono", 20, italic=True)
player = quicksand60.render('{ NEO PLAYER }', True, (255, 255, 255))

# Menu:

display.set_caption('NEO PLAYER')
opt1 = quicksand22.render('1  |  Megadeth - Holy Wars', True, (250, 250, 250))
opt2 = quicksand22.render('2  |  Eluveitie  - Tegernakô', True, (250, 250, 250))
opt3 = quicksand22.render('3  |  Metallica  - Fuel', True, (250, 250, 250))
opt4 = quicksand22.render('4  |  Metallica  - One', True, (250, 250, 250))
opt5 = quicksand22.render('5  |  Metallica  - Enter Sandman', True, (250, 250, 250))
opt6 = quicksand22.render('6  |  Metallica  - The Unforgiven', True, (250, 250, 250))
opt7 = quicksand22.render('7  |  Metallica  - Nothing Else Matters', True, (250, 250, 250))
opt8 = quicksand22.render('8  |  Metallica  - Fade to Black', True, (250, 250, 250))
opt9 = quicksand22.render('9  |  Metallica  - For Whom the Bell Tolls', True, (250, 250, 250))
options = [opt1, opt2, opt3, opt4, opt5, opt6, opt7, opt8, opt9]
"""dur = s / 61.95
minu = int(dur)
seg = int((dur - minu) * 10)
seg2 = int((dur * 10 - int(dur * 10)) * 10)
dur_m = notomono22.render(f'| {minu}:{seg}{seg2}', True, (250, 250, 250))"""
author = notomono20_italic.render('By $Neo', True, (180, 170, 160))


def playing(i):
    v = pp = 1
    color_change = img_alpha_change = p2 = 0
    n = 5
    m = 8
    playpausex = 66
    playpausey = 642
    playpausesize = 38
    z = 10
    playrun = True
    clicking = False
    pr = 110
    clock = pg.time.Clock()
    while playrun:
        song_pos = mixer.music.get_pos() // 1000
        mx1, my1 = pg.mouse.get_pos()
        busy1 = mixer.get_busy
        for event1 in pg.event.get():
            if event1.type == pg.QUIT:
                playrun = False
            if 70 < mx1 < 104:
                if 648 < my1 < 680:
                    playpausex = 65.5
                    playpausey = 641.7
                    playpausesize = 40
                else:
                    playpausex = 66
                    playpausey = 642
                    playpausesize = 38
            elif pr < mx1 < pr + 25:
                if 648 < my1 < 680:
                    m = 10
                else:
                    m = 8
            else:
                playpausex = 66
                playpausey = 642
                playpausesize = 38
                m = 8
            if event1.type == MOUSEBUTTONDOWN:
                button_number1 = event1.button
                if button_number1 == 1:
                    if pr < mx1 < pr + 25:
                        if 648 < my1 < 680:
                            m = 11
                            clicking = True
                    if 70 < mx1 < 104:
                        if 648 < my1 < 680:
                            if pr >= 718:
                                mixer.music.stop()
                                mixer.music.play(0, 0)
                                pr = 110
                                pp = 1
                            else:
                                if p2 % 2 == 0:
                                    mixer.music.pause()
                                    p2 += 1
                                    pp = 0
                                else:
                                    mixer.music.unpause()
                                    p2 += 1
                                    pp = 1
            if event1.type == MOUSEBUTTONUP:
                button_number1 = event1.button
                if color_change >= 60:
                    if button_number1 == 1:
                        if pr > 718:
                            mixer.music.stop()
                            pr = 718
                        divi = 720 / s
                        n = pr / divi
                        print(s, n)
                        if n > s:
                            n = s
                        mixer.music.play(0, n)
                        clicking = False
                        if pr < 115:
                            pr = 110
                            mixer.music.play()
            if event1.type == KEYDOWN:
                key1 = pg.key.get_pressed()
                if key1[pg.K_RIGHT]:
                    divi = 736 / s
                    n = pr / divi
                    pr += divi * 5
                    mixer.music.play(0, n)
                    if pr > 718:
                        pr = 718
                if key1[pg.K_LEFT]:
                    divi = 736 / s
                    n = - (pr / divi)
                    pr -= divi * 5
                    mixer.music.play(0, n)
                    if pr < 115:
                        pr = 110
                if key1[pg.K_ESCAPE]:
                    z = - 3
                    mixer.music.stop()
                    playrun = False
                if p2 % 2 == 0:
                    if key1[pg.K_SPACE]:
                        if pr >= 818:
                            mixer.music.play()
                            pr = 110
                            pp = 1
                        else:
                            mixer.music.pause()
                            p2 += 1
                            pp = 0
                else:
                    if key1[pg.K_SPACE]:
                        mixer.unpause()
                        p2 += 1
                        pp = 1
                if key1[pg.K_KP_PLUS]:
                    v += 0.1
                    if v >= 1:
                        v = 1
                    song.set_volume(v)
                if key1[pg.K_KP_MINUS]:
                    v -= 0.1
                    if v <= 0:
                        v = 0
                    song.set_volume(v)
        clock.tick()
        d = 10.33 / s
        pr += d
        if clicking:
            pr = mx1 - 15
            if pr > 718:
                pr = 718
            if pr < 115:
                pr = 110
        if not clicking:
            pr += d
        color_change += z
        img_alpha_change += 10
        if img_alpha_change > 255:
            img_alpha_change = 255
        if color_change > 60:
            color_change = 60
        if color_change < 0:
            color_change = 0
        if p2 % 2 != 0:
            pr -= d
        if pr > 718:
            pr = 718
            pp = 0
        rect1_size = (860, 160)
        rect2_size = (860, 39)
        rect3_size = (710, 49)
        transp = pg.Surface(rect1_size, pg.SRCALPHA)
        barra_transp = pg.Surface(rect2_size, pg.SRCALPHA)
        barra_transp2 = pg.Surface(rect3_size, pg.SRCALPHA)
        # Music screen:
        voltar = notomono16.render('* ESC = Menu', True, (color_change + 120, color_change + 120, color_change + 120))
        tithol = quicksand38.render('Megadeth - Holy Wars', True, (200, 200, 200))
        titteg = quicksand38.render('Eluveitie - Tegernakô', True, (255, 255, 255))
        fuel = quicksand38.render('Metallica - Fuel', True, (255, 255, 255))
        one = quicksand38.render('Metallica - One', True, (255, 255, 255))
        entersandman = quicksand38.render('Metallica - Enter Sandman', True, (255, 255, 255))
        theunforgiven = quicksand38.render('Metallica - The Unforgiven', True, (255, 255, 255))
        nothingelsematters = quicksand38.render('Metallica - Nothing Else Matters', True, (255, 255, 255))
        fadetoblack = quicksand38.render('Metallica - Fade to Black', True, (255, 255, 255))
        forwhomthebelltolls = quicksand38.render('Metallica - For Whom the Bell Tolls', True, (255, 255, 255))
        tits = [tithol, titteg, fuel, one, entersandman, theunforgiven, nothingelsematters, fadetoblack,
                forwhomthebelltolls]
        volume = quicksand22.render(f'|            Volume {int(v * 100)}%', True, (255, 255, 255))
        branco = (color_change, color_change, color_change)
        azul_escuro = (0, 0, 100)
        preto_transp = (0, 0, 0, 180)
        azul_escuro_transp = (0, 0, 50, 200)
        screen.fill((0, 0, 0))
        # Retângulo grande preto transparente:
        pg.draw.rect(transp, preto_transp, transp.get_rect(), 0)
        # Capas dos álbuns:
        imgs[i].set_alpha(img_alpha_change)
        screen.blit(imgs[i], (0, 0))
        screen.blit(transp, (0, 600))
        # Retângulo azul:
        pg.draw.rect(barra_transp, azul_escuro_transp, barra_transp.get_rect(), 0)
        # Retângulo preto transparente:
        pg.draw.rect(barra_transp2, preto_transp, barra_transp2.get_rect(), 0, border_radius=20)
        screen.blit(barra_transp, (0, 580))
        screen.blit(barra_transp2, (57, 636))
        # Títulos das músicas:
        screen.blit(tits[i], (70, 572))
        screen.blit(voltar, (660, 690))
        # Barra de progresso branca:
        pg.draw.rect(screen, branco, (120, 661, 618, 3), border_radius=20)
        # Barra de progresso azul:
        pg.draw.rect(screen, azul_escuro, (120, 661, pr - 110, 3))
        # Bola da barra de progresso:
        pg.draw.circle(screen, azul_escuro, center=(pr + 15, 662), radius=m)
        # Volume:
        screen.blit(volume, (620, 585))
        # Quadrado azul atrás do play/pause:
        pg.draw.rect(screen, azul_escuro, (playpausex + 1, playpausey + 1, playpausesize - 1, playpausesize - 1),
                     border_radius=12)
        if pp == 1:
            pg.draw.rect(screen, (220, 220, 220), (playpausex + 10, playpausey + 8, playpausesize - 32, playpausesize - 15))
            pg.draw.rect(screen, (220, 220, 220), (playpausex + 23, playpausey + 8, playpausesize - 32, playpausesize - 15))
        if pp == 0:
            pg.draw.polygon(screen, (220, 220, 220), points=
            ((playpausex + 12, 649), (playpausex + 12, playpausesize + 633), (98, 661)))
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
        if 290 < my < 330:
            t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t0 = 150
        elif 334 < my < 374:
            t0 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t1 = 150
        elif 378 < my < 408:
            t0 = t1 = t3 = t4 = t5 = t6 = t7 = t8 = 60
            t2 = 150
        elif 412 < my < 452:
            t0 = t1 = t2 = t4 = t5 = t6 = t7 = t8 = 60
            t3 = 150
        elif 456 < my < 496:
            t0 = t1 = t2 = t3 = t5 = t6 = t7 = t8 = 60
            t4 = 150
        elif 500 < my < 540:
            t0 = t1 = t2 = t3 = t4 = t6 = t7 = t8 = 60
            t5 = 150
        elif 544 < my < 584:
            t0 = t1 = t2 = t3 = t4 = t5 = t7 = t8 = 60
            t6 = 150
        elif 588 < my < 628:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t8 = 60
            t7 = 150
        elif 632 < my < 672:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = 60
            t8 = 150
        else:
            t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
    else:
        t0 = t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = 60
    busy = mixer.get_busy()
    songs = ['./assets/holywars.ogg', './assets/tegernako.ogg', './assets/Metallica - Fuel (Official Music Video).ogg',
             './assets/Metallica: One (Official Music Video).ogg',
             './assets/Metallica: Enter Sandman (Official Music Video).ogg',
             './assets/Metallica - The Unforgiven (Official Music Video).ogg',
             './assets/Metallica: Nothing Else Matters (Official Music Video).ogg', './assets/Fade To Black.ogg',
             './assets/For Whom The Bell Tolls.ogg']
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        key = pg.key.get_pressed()
        if key[pg.K_ESCAPE]:
            run = False
        key = pg.key.get_pressed()
        if event.type == MOUSEBUTTONDOWN:
            button_number = event.button
            if button_number == 1:
                if 30 < mx < 830:
                    if 290 < my < 330:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 295))
                        display.update()
                        p = i = t = 0
                        mixer.music.load(songs[i])
                        som = mixer.Sound(songs[i])
                        song = som
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 332 < my < 372:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 337))
                        display.update()
                        p = i = t = 1
                        mixer.music.load(songs[i])
                        som2 = mixer.Sound(songs[i])
                        song = som2
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 374 < my < 414:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 379))
                        display.update()
                        p = i = t = 2
                        mixer.music.load(songs[i])
                        som3 = mixer.Sound(songs[i])
                        song = som3
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 416 < my < 456:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 421))
                        display.update()
                        p = i = t = 3
                        mixer.music.load(songs[i])
                        som4 = mixer.Sound(songs[i])
                        song = som4
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 458 < my < 498:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 463))
                        display.update()
                        p = i = t = 4
                        mixer.music.load(songs[i])
                        som5 = mixer.Sound(songs[i])
                        song = som5
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 500 < my < 540:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 505))
                        display.update()
                        p = i = t = 5
                        mixer.music.load(songs[i])
                        som6 = mixer.Sound(songs[i])
                        song = som6
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 542 < my < 582:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 547))
                        display.update()
                        p = i = t = 6
                        mixer.music.load(songs[i])
                        som7 = mixer.Sound(songs[i])
                        song = som7
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 584 < my < 624:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 589))
                        display.update()
                        p = i = t = 7
                        mixer.music.load(songs[i])
                        som8 = mixer.Sound(songs[i])
                        song = som8
                        s = song.get_length()
                        mixer.music.play()
                        playing(i)
                    if 626 < my < 666:
                        loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
                        screen.blit(loading, (430, 631))
                        display.update()
                        p = i = t = 8
                        mixer.music.load(songs[i])
                        som9 = mixer.Sound(songs[i])
                        song = som9
                        s = song.get_length()
                        mixer.music.play()
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
        screen.blit(options[k], (20, y + (k * 42)))
    #screen.blit(dur_m, (735, 296))
    screen.blit(author, (750, 680))
    display.update()
