import pygame as pg
from pygame import mixer, image, display, transform
pg.init()
mixer.init()
v = 1
p = i = t = c = 0
screen = display.set_mode((860, 710), vsync=1)
holy_img = transform.scale(image.load('megadeth.jpg'), (650, 550))
teger_img = transform.scale(image.load('tegernako.jpg'), (650, 550))
back = transform.scale(image.load('land.jpeg'), (850, 700))
ball = transform.scale(image.load('circle.png'), (25, 25))
imgs = [holy_img, teger_img]
pg.font.init()
helvetica45 = pg.font.SysFont("notomono", 45)
helvetica35 = pg.font.SysFont("notomono", 35)
helvetica30 = pg.font.SysFont("notomono", 30, italic=True)
helvetica25 = pg.font.SysFont("notomono", 25, italic=True)
helvetica20 = pg.font.SysFont("notomono", 20)
helvetica16 = pg.font.SysFont("notomono", 16)
helvetica20_italic = pg.font.SysFont("notomono", 20, italic=True)
player = helvetica45.render('{ NEO PLAYER }', True, (0, 0, 0))
# Tela Inicial:
display.set_caption('NEO PLAYER')
opcao1 = helvetica25.render('1 - "Megadeth - Holy Wars"', True, (220, 220, 220))
opcao2 = helvetica25.render('2 - "Eluveitie - Tegernakô"', True, (220, 220, 220))
selecione = helvetica16.render('*Selecione a música pelo número', True, (200, 200, 200))
author = helvetica20_italic.render('By $Neo', True, (180, 170, 160))
# Tela da música:
voltar = helvetica16.render('* ESC = Menu', True, (20, 20, 20))
tithol = helvetica35.render('Megadeth - Holy Wars', True, (20, 20, 20))
titteg = helvetica35.render('Eluveitie - Tegernakô', True, (20, 20, 20))
tits = [tithol, titteg]
play = pg.image.load('play.png')
pause = pg.image.load('pause.png')
play_pause = [play, pause]
# Músicas:
som = mixer.Sound('holywars.ogg')
som2 = mixer.Sound('tegernako.ogg')
sons = [som, som2]
som.set_volume(v)
run = True


def rel(i):
    v = 1
    p = pp = 0
    run = True
    pr = 120
    clock = pg.time.Clock()
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            key = pg.key.get_pressed()
            if event.type == pg.KEYDOWN:
                if key[pg.K_ESCAPE]:
                    run = False
                    for i in range(0, len(sons)):
                        sons[i].stop()
                    print('Exiting...')
                if key[pg.K_1]:
                    i = 0
                    sons[i].stop()
                    sons[i].play()
                    print('Playing "Megadeth - Holy Wars"')
                if key[pg.K_2]:
                    som2.stop()
                    som.stop()
                    som2.play()
                    p = 0
                    print('Playing "Eluveitie - Tegernakô"')
                if p % 2 == 0:
                    if key[pg.K_SPACE]:
                        mixer.pause()
                        p += 1
                        pp = 1
                        print('Pause')
                else:
                    if key[pg.K_SPACE]:
                        mixer.unpause()
                        p += 1
                        pp = 0
                        print('Resume')
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
                if v >= 1:
                    v = 1
                    print('Volume Max')
                if v <= 0:
                    v = 0
                    print('Volume Min')
        clock.tick(100)
        s = sons[i].get_length()
        d = 6 / s
        pr += d
        if p % 2 != 0:
            pr -= d
        if pr > 690:
            pr = 690
        volume = helvetica20.render(f'Volume {int(v * 100)}%', True, (20, 20, 20))
        preto = (0, 0, 0)
        sombra = (60, 60, 60)
        screen.fill((140, 140, 140))
        screen.blit(imgs[i], (103, 40))
        screen.blit(tits[t], (103, 600))
        screen.blit(voltar, (600, 690))
        pg.draw.rect(screen, preto, (120, 661, 600, 3))
        screen.blit(ball, (pr, 650))
        screen.blit(volume, (620, 610))
        screen.blit(play_pause[pp], (94, 650))
        pg.display.update()


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
                    p = i = t = 0
                    sons[i].play()
                    print('Playing "Megadeth - Holy Wars"')
                    rel(i)
                if key[pg.K_2] or key[pg.K_KP_2]:
                    p = 0
                    t = i = 1
                    som2.play()
                    print('Playing "Eluveitie - Tegernakô"')
                    rel(i)

    screen.fill((0, 10, 25))
    screen.blit(back, (5, 5))
    screen.blit(player, (250, 80))
    screen.blit(opcao1, (100, 450))
    screen.blit(opcao2, (100, 500))
    screen.blit(selecione, (50, 680))
    screen.blit(author, (750, 680))
    display.update()
