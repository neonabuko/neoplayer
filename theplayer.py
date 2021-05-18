#!/usr/bin/env python3

# Bibliotecas:

from tinytag import TinyTag
from threading import Event
import os
import time
import datetime
import pygame as pg
from pygame import mixer, image, display, transform
from pygame.locals import *
pg.init()
mixer.init()
exit = Event()
screen = display.set_mode((860, 720), vsync=1)

# Imagens:

back = transform.scale(image.load('./assets/back.jpg'), (860, 720))
back2 = transform.scale(image.load('./assets/back.jpg'), (1060, 559))
player_icon = transform.scale(image.load('./assets/player_back.jpg'), (100, 100))

# Fontes:

pg.font.init()
quicksand80 = pg.font.SysFont("quicksand", 80)
notomono35 = pg.font.SysFont("notomono", 35)
notomono30_italic = pg.font.SysFont("notomono", 30, italic=True)
quicksand22 = pg.font.SysFont("quicksand", 22)
notomono22 = pg.font.SysFont("notomono", 22)
quicksand20 = pg.font.SysFont("quicksand", 20, bold=True)
quicksand20n = pg.font.SysFont("quicksand", 20)
quicksand16 = pg.font.SysFont('quicksand', 16, italic=True)
notomono20_italic = pg.font.SysFont("notomono", 20, italic=True)

#---------------------------------- Textos do Menu Inicial -------------------------------------#

display.set_caption('NEO PLAYER')
display.set_icon(player_icon)
player = quicksand80.render('{ NEO PLAYER }', True, (220, 220, 220))
player3 = quicksand80.render('{ NEO PLAYER }', True, (0, 0, 180))
player2 = quicksand80.render('{ NEO PLAYER }', True, (0, 0, 0))
author = quicksand16.render('by $Neo', True, (255, 255, 255))
num_mus = 1
songs = []
options = []
nomes_tits = []
tits = []
dur_mus = []
tams_fontes = []
with os.scandir('./assets') as entries:
	for entry in entries:
		if '.ogg' in entry.name:
			songs.append('./assets/' + entry.name)
			name = entry.name
			name = name.replace('.ogg', '')
			tag = TinyTag.get('./assets/' + entry.name)
			dur = int(tag.duration)
			conversion = datetime.timedelta(seconds=dur)
			durf = str(conversion)
			dur_mus.append(quicksand20n.render(f'{durf}', True, (255, 255, 255)))
			options.append(quicksand20.render(f'{num_mus}   |   {name}', True, (255, 255, 255)))
			nomes_tits.append(name)
			num_mus += 1

capa = transform.scale(image.load('./assets/player_back.jpg'), (1720, 720))
#----------Função "música tocando"-----------#

def playing(i):
	v = 1
	pause = False
	color_change = p2 = n = cor_tits = 0
	img_alpha_change = 1
	m = 0
	playpausex = 0
	playpausey = 676
	playpausesize = 32
	z = 10
	playrun = True
	clicking = False
	pr = 50
	
# Loop da função:
	while playrun:
		clock = pg.time.Clock()
		mx1, my1 = pg.mouse.get_pos()
		for event1 in pg.event.get():
			if event1.type == pg.QUIT:
				playrun = False
				
		# Mouse sobre play/pause:
			if 8 < mx1 < 41:
				if 680 < my1 < 720:
					playpausex = - 1
					playpausey = 675
					playpausesize = 34
				else:
					playpausex = 0
					playpausey = 676
					playpausesize = 32
					
		# Mouse sobre a bolinha azul:
			elif pr < mx1 < pr + 20:
				if 692 < my1 < 708:
					m = 10
				else:
					m = 0
			else:
				playpausex = 0
				playpausey = 676
				playpausesize = 32
				m = 0
			if event1.type == MOUSEBUTTONDOWN:
				button_number1 = event1.button
				if button_number1 == 1:
				
				# Clicando na bolinha azul:
					if pr - 3 < mx1 < pr + 17:
						if 692 < my1 < 708:
							m = 11
							clicking = True
							
				# Clicando na barra de progresso:
					elif pr + 17 < mx1 < 668 or 50 < mx1 < pr + 17:
						if 692 < my1 < 708:
							clicking = True
					else:
						clicking = False
						
				# Clicando no play/pause:
					if 8 < mx1 < 41:
						if 680 < my1 < 720:
							if pr >= 654:
								mixer.music.stop()
								mixer.music.play()
								pr = 50
								pause = False
							else:
								if not pause:
									mixer.music.pause()
									p2 += 1
									pause = True
								elif pause:
									mixer.music.unpause()
									p2 += 1
									pause = False
									
		# Soltando o clique:
			if event1.type == MOUSEBUTTONUP:
				button_number1 = event1.button
				if color_change >= 60:
					if button_number1 == 1:
						if clicking:
							prt = pr - 50
							if prt <= 0:
								prt = 0
								mixer.music.play()
								pause = False
							if prt >= 610:
								mixer.music.stop()
								prt = 610
								pause = True
							if prt < 610:
								divi = 610 / s
								pos_mus = prt / divi
								n = pos_mus
								mixer.music.play(0, n)
								pause = False
							if mx1 < 50:
								pr = 50
							if mx1 >= 50:
								pr = mx1 - 7
							clicking = False
							
#------------------Apertando teclas---------------#

			if event1.type == KEYDOWN:
				key1 = pg.key.get_pressed()
				if key1[pg.K_RIGHT]:
					divi = 610 / s
					prt = pr - 50
					pos_mus = prt / divi
					if pos_mus == s:
						mixer.music.stop()
						pause = True
						prt = 610
					if pos_mus < pos_mus - 5:
						n += 5
						pr += divi * 5
						mixer.music.play(0, n)
				if key1[pg.K_LEFT]:
					pause = False
					prt = pr - 50
					divi = 610 / s
					if prt > 0:
						n -= 5
					if n < 0:
						n = 0
					pr -= divi * 5
					mixer.music.play(0, n)
					if pr < 50:
						pr = 50
				if key1[pg.K_ESCAPE]:
					z -= 20
					ç = 0
					pause = True
					mixer.music.stop()
				if not pause:
					if key1[pg.K_SPACE]:
						if pr >= 654:
							mixer.music.play()
							pr = 50
							pause = False
						else:
							mixer.music.pause()
							p2 += 1
							pause = True
				elif pause:
					if key1[pg.K_SPACE]:
						mixer.music.unpause()
						p2 += 1
						pause = False
				if key1[pg.K_KP_PLUS] or key1[pg.K_UP]:
					v += 0.1
					if v >= 1:
						v = 1
					pg.mixer.music.set_volume(v)
				if key1[pg.K_KP_MINUS] or key1[pg.K_DOWN]:
					v -= 0.1
					if v <= 0:
						v = 0
					pg.mixer.music.set_volume(v)
					
    # Velocidade da bolinha azul:
		clock.tick(60)
		d = 604 / s
		if clicking:
			pr = mx1 - 7
			m = 11
			if pr > 654:
				pr = 654
			if pr < 50:
				pr = 50
		if not clicking:
			pr += d / 60
			if pr < 0:
				pr = 0
		if pause:
			pr -= d / 60
		elif not pause:
			pr += d / 60
		if pr > 660:
			pr = 660
			pause = True
			mixer.music.stop()
		color_change += z
		img_alpha_change += 3.5 * z
		if img_alpha_change > 255:
			img_alpha_change = 255
		if img_alpha_change <= 0:
			playrun = False

		if color_change > 80:
			color_change = 80
		if color_change < 0:
			color_change = 0
		
#-------------------------------------------------------- Tela da música ----------------------------------------------------------------#
		
		rect1_size = (860, 185)
		rect2_size = (860, 41)
		rect3_size = (630, 20)
		transp = pg.Surface(rect1_size, pg.SRCALPHA)
		barra_transp = pg.Surface(rect2_size, pg.SRCALPHA)
		barra_transp2 = pg.Surface(rect3_size, pg.SRCALPHA)
		play_icon = transform.scale(image.load('./assets/play.png'), (playpausesize + 13, playpausesize + 13))
		pause_icon = transform.scale(image.load('./assets/pause.png'), (playpausesize + 13, playpausesize + 13))
		branco = (color_change * 1.8, color_change * 1.8, color_change * 1.8)		
		volume = quicksand20.render(f'Volume {int(v * 100)}%', True, (color_change * 3, color_change * 3, color_change * 3))
		azul_escuro = (0, 0, color_change * 1.8)
		azul_medio = (0, 0, color_change * 2)
		preto_transp = (0, 0, 0, color_change * 2.6)
		azul_escuro_transp = (0, 0, 50, color_change * 2.5)
		screen.fill((0, 0, 0))
	
	# Retângulo grande preto transparente:		
		pg.draw.rect(transp, preto_transp, transp.get_rect(), 0)
		
	# Capas dos álbuns:
		capa.set_alpha(img_alpha_change)
		screen.blit(capa, (- 700, - 85))
		screen.blit(transp, (0, 633))
		
	# Retângulo azul:		
		pg.draw.rect(barra_transp, azul_escuro_transp, barra_transp.get_rect(), 0)
		
	# Retângulo preto transparente:		
		pg.draw.rect(barra_transp2, preto_transp, barra_transp2.get_rect(), 0, border_radius=10)
		screen.blit(barra_transp, (0, 635))
		screen.blit(barra_transp2, (45, 690))
	# Títulos das músicas:
		dtext = 38 - tams_fontes[i]
		if dtext > 9:
			dtext = 9		
		screen.blit(tits[i], (10, 629 + dtext))
		
	# Barra de progresso branca:		
		pg.draw.rect(screen, branco, (50, 698.5, 618, 3))
		
	# Barra de progresso azul:		
		pg.draw.rect(screen, azul_escuro, (50, 698.5, pr - 42, 3))
		
	# Bola da barra de progresso:		
		pg.draw.circle(screen, azul_medio, center=(pr + 7, 699), radius=m)
		
	# Volume:		
		screen.blit(volume, (708, 683))
		if not pause:
			screen.blit(pause_icon, (playpausex + 1, playpausey - 5))
		if pause:
			screen.blit(play_icon, (playpausex + 1, playpausey - 5))
		pg.display.update()

button_number = i = ç = q = w = g = c = 0
çn = 15
y = 168
yt = 160
tp = []
lista = []
run = True
exiting = False

for k in range(0, len(nomes_tits)):
	tam_fonte = (1680 // len(nomes_tits[k]))
	if tam_fonte > 38:
		tam_fonte = 38
	if tam_fonte < 20:
		tam_fonte = 20
	tams_fontes.append(tam_fonte)
	quicksand38 = pg.font.SysFont("quicksand", tams_fontes[k])
	tits.append(quicksand38.render(f'{nomes_tits[k]}', True, (220, 220, 220)))
for k in range(0, len(songs)):
	tp.append(40)
	
#---------------------------------------------- Loop do Menu Inicial --------------------------------------------------#

while run:
	mouse = pg.mouse.get_pressed(num_buttons=5)
	mx, my = pg.mouse.get_pos()
	
# Passando o mouse por cima das opções:
	if 10 < mx < 850:
		if 160 < my < 720:
			for c in range(0, len(songs)):
				lista.append(list(range((yt + (c * 42)), (yt + 42 + (c * 42)))))
				tp.pop(c)
				tp.insert(c, 40)
				if (my + (w * 25)) in lista[c]:
					q = c
					tp.pop(q)
					tp.insert(q, 180)
	if my < 160 or my > 718 or mx > 850 or 10 > mx:
		tp.pop(q)
		tp.insert(q, 40)
		tp[0:len(songs)] = tp	
		exit.wait(0.08)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		key = pg.key.get_pressed()
		if key[pg.K_ESCAPE]:
			çn = - 20
			exit.set()
			exiting = True
			
	# Clicando nas opções:
		if event.type == MOUSEBUTTONDOWN:
			button_number = event.button
			if button_number == 1:
				if 30 < mx < 830:
					for c in range(0, len(songs)):
						lista.append(list(range((yt + (c * 43)), (yt + 41 + (c * 41)))))
						if (my + (w * 25)) in lista[c]:
							i = c
							loading = quicksand22.render('Loading . . .', True, (0, 250, 0))
							screen.blit(loading, (520, yt + 5 + (i * 42)))
							display.update()
							p = t = ç = 0
							mixer.music.load(songs[c])
							som = mixer.Sound(songs[c])
							song = som
							s = song.get_length()
							mixer.music.play()
							mixer.music.queue(songs[c])
							playing(i)
			if button_number == 4:
				if (yt + (k * 42)) > 670:
					yt -= 25
					y -= 25
					w += 1
			if button_number == 5:
				if yt < 160:
					yt += 25
					y += 25
					w -= 1

	ç += çn
	if ç > 100:
		ç = 100
	if ç < 0 and exiting:
		run = False
	screen.fill((0, 0, 10))
	back.set_alpha(ç)
	back2.set_alpha(245)
	screen.blit(back, (0, 0))
	rect_size = (840, 40)
	barra_azul_transp = pg.Surface(rect_size, pg.SRCALPHA)
	transps = []
	if not exiting:
		for k in range(0, len(songs)):
			pg.draw.rect(barra_azul_transp, (0, 30, 120, tp[k]), barra_azul_transp.get_rect(), 20, border_radius=5)
			transps.append(barra_azul_transp)
			screen.blit(transps[k], (10, yt + (k * 42)))
		for k in range(0, len(options)):
			screen.blit(options[k], (20, y + (k * 42)))
			screen.blit(dur_mus[k], (765, y + (k * 42)))
		screen.blit(back2, (-100, - 410))
		screen.blit(player3, (125, 26))
		screen.blit(player2, (124, 25))		
		screen.blit(player, (123, 20))
		screen.blit(author, (585, 110))
	elif exiting:
		screen.blit(player3, (125, 306))
		screen.blit(player2, (124, 305))
		screen.blit(player, (123, 300))
	display.update()
pg.quit()

