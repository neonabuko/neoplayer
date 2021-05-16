import pygame as pg
pg.init()
x = 0
back = pg.transform.scale(pg.image.load('./assets/back.jpg'), (860, 720))
while x < 720:
	x += 20
	screen = pg.display.set_mode((860, x))
	screen.fill((150, 0, 0))
	screen.blit(back, (0, 0))
	pg.display.update()
run = True
while run:
	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			key = pg.key.get_pressed()
			if key[pg.K_ESCAPE]:
				while x > 0:
					x -= 20
					screen = pg.display.set_mode((860, x))
					pg.display.update()
					if x == 0:
						run = False
	screen.fill((0, 150, 0))
	screen.blit(back, (0, 0))
	pg.display.update()
