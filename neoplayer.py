#!/usr/bin/env python3

# Bibliotecas/Verificação de bibliotecas:

import os
done = 0
op_sys = os.name

with os.scandir('.') as entries:
	for entry in entries:
		if 'installation_register' in entry.name:
			done += 1
if done < 1:
	print("Installing Python libraries...")
	print()
	if op_sys == 'posix':
		os.system('pip install -r requirements.txt && touch installation_register')
	elif op_sys == 'nt':
		os.system('py -m pip install -r requirements.txt && cd.> installation_register.txt')
	print('Installation done')
	print()
elif done >= 1:
	print()
	print('Welcome to Neo Player!')
	print()

from tinytag import TinyTag
from threading import Event
import time
import datetime
import pygame as pg
from pygame import mixer, image, display, transform
from pygame.locals import *
import multiprocessing as mp

# Iniciando o pygame:

pg.init()
exit = Event()
screen = display.set_mode((860, 720))

# Imagens:

back = transform.scale(image.load('./assets/back.jpg'), (860, 720))
back2 = transform.scale(image.load('./assets/back.jpg'), (1060, 559))
player_icon = transform.scale(image.load('./assets/player_back.jpg'), (100, 100))

# Fontes dos textos:

pg.font.init()
quicksand80 = pg.font.SysFont("quicksand", 80)
notomono35 = pg.font.SysFont("notomono", 35)
notomono30_italic = pg.font.SysFont("notomono", 30, italic=True)
quicksand22 = pg.font.SysFont("quicksand", 22)
quicksand22b = pg.font.SysFont("quicksand", 22, bold=True)
notomono22 = pg.font.SysFont("notomono", 22)
quicksand20 = pg.font.SysFont("quicksand", 20, bold=True)
quicksand20n = pg.font.SysFont("quicksand", 20)
quicksand16 = pg.font.SysFont('quicksand', 16, italic=True)
notomono20_italic = pg.font.SysFont("notomono", 20, italic=True)

# Textos do Menu Inicial:

display.set_caption('NEO PLAYER')
display.set_icon(player_icon)
player = quicksand80.render('{ NEO PLAYER }', True, (220, 220, 220))
player3 = quicksand80.render('{ NEO PLAYER }', True, (0, 0, 180))
player2 = quicksand80.render('{ NEO PLAYER }', True, (0, 0, 0))
author = quicksand16.render('by $Neo', True, (255, 255, 255))
loading = quicksand22b.render('Loading . . .', True, (0, 250, 0))
capa = transform.scale(image.load('./assets/player_back.jpg'), (1720, 720))

#---------- Função "música tocando" -----------#


def playing(i):
	v = 1
	color_change = n = 0
	img_alpha_change = 1
	m = 0
	z = 10
	
# Play/pause x, y, size:

	ppx = 395
	ppy = 655
	pps = 50
	
# Next x, y, size:

	nx = 455
	ny = 665
	ns = 32
	
# Previous x, y, size:

	pvx = 350
	pvy = 665
	pvs = 32
	
# Booleans:	

	playrun = True
	clicking = False
	nclicking = False
	pclicking = False
	pause = False
	
	pr = 10
	seg = 0
	minu = 0
	mixer.init()
	mixer.music.load(songs[i])
	mixer.music.play()
	som = mixer.Sound(songs[i])
	song = som
	s = song.get_length()
	nn = 0
	ppclicking = False
	
# Loop da função:

	while playrun:
		mus_pos = mixer.music.get_pos() / 1000
		mx1, my1 = pg.mouse.get_pos()
		rtx = rty = 0
		rtsize = 40
		
	# Mouse sobre o botão de return:
	
		if 0 < mx1 < 42 and 0 < my1 < 42:
			rtx = rty = - 2
			rtsize = 47
		return_button = transform.scale(image.load('./assets/return2.png'), (rtsize, rtsize))
		
	# Mouse sobre play/pause:
	
		if 394 < mx1 < 446 and 654 < my1 < 706 and not ppclicking:
			ppx = 394
			ppy = 654
			pps = 52
		else:
			ppx = 395
			ppy = 655
			pps = 50
		play_icon = transform.scale(image.load('./assets/play.png'), (pps, pps))
		pause_icon = transform.scale(image.load('./assets/pause.png'), (pps, pps))
		previous_icon = transform.scale(image.load('./assets/previous.png'), (ns, ns))
		
	# Mouse sobre o botão next:
	
		if 453 < mx1 < 487 and 655 < my1 < 689 and not nclicking:
			nx = 454
			ny = 664
			ns = 35
		else:
			nx = 455
			ny = 665
			ns = 32
		next_icon = transform.scale(image.load('./assets/next.png'), (ns, ns))
		
	# Mouse sobre o botão previous:
	
		if 349 < mx1 < 383 and 655 < my1 < 689 and not pclicking:
			pvx = 349
			pvy = 664
			pvs = 35
		else:
			pvx = 350
			pvy = 665
			pvs = 32
		previous_icon = transform.scale(image.load('./assets/previous.png'), (pvs, pvs))			
			
	# Mouse sobre a bolinha azul:
	
		if pr - 20 < mx1 < pr + 20 and 698 < my1 < 720:
			m = 7
		else:
			m = 0
		for event1 in pg.event.get():
			if event1.type == pg.QUIT:
				playrun = False
			if event1.type == MOUSEBUTTONDOWN:
				button_number1 = event1.button
				if button_number1 == 1:
				
				# Clicando no botão de return:
				
					if 10 < mx1 < 40 and 10 < my1 < 40:
						mixer.music.stop()
						pause = True
						playrun = False
						
				# Clicando na bolinha azul:
				
					if pr - 15 < mx1 < pr + 15 and 705 < my1 < 720:
						m = 8
						clicking = True
							
				# Clicando na barra de progresso:
				
					elif pr + 15 < mx1 < 850 or 10 < mx1 < pr - 15:
						if 705 < my1 < 720:
							clicking = True
						
				# Clicando no play/pause:
				
					if 394 < mx1 < 449 and 654 < my1 < 708 and pr >= 849 and not clicking:
						mixer.music.stop()
						mixer.music.play()
						pr = 50
						nn = 0
						pause = False
					elif 394 < mx1 < 449 and 654 < my1 < 708 and pr < 849:
						ppclicking = True
							
				# Clicando no botão next:
				
					if 453 < mx1 < 485 and 655 < my1 < 689:
						nclicking = True
				
				# Clicando no botão previous:
				
					if 349 < mx1 < 383 and 655 < my1 < 689:
						pclicking = True		
							
		# Soltando o clique:
		
			if event1.type == MOUSEBUTTONUP:
				button_number1 = event1.button
				if color_change >= 80 and button_number1 == 1 and clicking:
					clicking = False
					prt = pr - 14
					if pr <= 10:
						pr = 10
						mixer.music.play()
						pause = False
					if pr >= 849:
						mixer.music.stop()
						pr = 849
						pause = True
					if mx1 <= 10: 	
						pr = 10
						n = 0
					if 10 < mx1 < 849:
						d = 840 / s
						n = prt / d
						nn = n - mus_pos
						mixer.music.set_pos(n)
						pr = mx1 - 4
						pause = False
				elif ppclicking and pr < 849:
					ppclicking = False
					if not pause:
						mixer.music.pause()
						pause = True
					elif pause:
						mixer.music.unpause()
						mixer.music.set_pos(mus_pos)
						pause = False
				elif nclicking:
					nclicking = False
					pr -= pr
					mixer.music.unload()
					mixer.quit()
					i += 1
					if i >= len(songs):
						i = 0
					playrun = False
					playing(i)
				elif pclicking:
					pr -= pr
					mixer.music.unload()
					mixer.quit()
					i -= 1
					if i < 0:
						i = len(songs) - 1
					playrun = False
					playing(i)
								
		# Apertando teclas:

			if event1.type == KEYDOWN:
				key1 = pg.key.get_pressed()
				if key1[pg.K_RIGHT]:
					divi = 814 / s
					prt = pr - 10
					pos_mus = prt / divi
					if pos_mus < s - 5:
						if pos_mus == s:
							mixer.music.stop()
							pause = True
							pr = 850
						n += 5
						pr += divi * 5
						mixer.music.play(i, n)
				if key1[pg.K_LEFT]:
					pause = False
					prt = pr - 10
					divi = 814 / s
					if pr > 10:
						n -= 5
					if n < 0:
						n = 0
					pr -= divi * 5
					if pr < 10:
						pr = 10
					mixer.music.play(i, n)
				if key1[pg.K_ESCAPE]:
					z -= 20
					fade = 0
					pause = True
				if not pause:
					if key1[pg.K_SPACE]:
						if pr >= 850:
							mixer.music.rewind()
							pr = 10
							pause = False
						else:
							mixer.music.pause()
							pause = True
				elif pause:
					if key1[pg.K_SPACE]:
						mixer.music.unpause()
						pause = False
				if key1[pg.K_KP_PLUS] or key1[pg.K_UP]:
					v += 0.1
					if v >= 1:
						v = 1
					pg.mixer.music.set_volume(v)
					screen.blit(volume, (708, 650))
				if key1[pg.K_KP_MINUS] or key1[pg.K_DOWN]:
					v -= 0.1
					if v <= 0:
						v = 0
					pg.mixer.music.set_volume(v)
					screen.blit(volume, (708, 650))
						
	# Velocidade da bolinha azul:
		if ppclicking:
			pps = 50
			ppx = 395
			ppy = 655
		if nclicking:
			nx = 455
			ny = 665
			ns = 32
		if pclicking:
			pvx = 350
			pvy = 665
			pvs = 32			
		d = 840 / s
		prt = pr - 10
	# Conversor do contador de tempo:
		if mus_pos + nn < s:
			pos_mus = mus_pos + nn
		if mus_pos <= 0:
			pos_mus = s
		seg = int(pos_mus)
		minu = int(pos_mus / 60)
		if seg >= minu * 60:
			seg -= minu * 60
		if clicking:	
			pr = mx1 - 4		
			m = 8
			if pr > 850:
				pr = 850
			elif pr < 10:
				pr = 10
		elif not clicking and not pause:
			pr = ((mus_pos + nn) * d) + 10
			if pr < 10:
				pr = 10
				mixer.music.stop()
				mixer.music.play()
		if pr > 849:
			pr = 849
			pause = True
			mixer.music.stop()
			
	# Variações de transparência:
	
		color_change += z
		img_alpha_change += 3.5 * z
		if img_alpha_change > 255:
			img_alpha_change = 255
		if img_alpha_change <= 0:
			playrun = False
			mixer.quit()
		if color_change > 80:
			color_change = 80
		if color_change < 0:
			color_change = 0
		
	# Tela da música:
		
		rect1_size = (860, 45)
		rect2_size = (860, 41)
		transp = pg.Surface(rect1_size, pg.SRCALPHA)
		barra_transp = pg.Surface(rect2_size, pg.SRCALPHA)
		branco = (color_change * 1.8, color_change * 1.8, color_change * 1.8)		
		volume = quicksand20.render(f'Volume {int(v * 100)}%', True, (color_change * 3, color_change * 3, color_change * 3))
		azul_escuro = (0, 0, color_change * 1.8)
		azul_medio = (0, 0, color_change * 2)
		preto_transp = (0, 0, 0, color_change * 1.5)
		azul_escuro_transp = (0, 0, 50, color_change * 2.5)
		screen.fill((0, 0, 0))
	
	# Retângulo grande preto transparente:		
		pg.draw.rect(transp, azul_escuro_transp, transp.get_rect(), 0)
		
	# Capas dos álbuns:
		capa.set_alpha(img_alpha_change)
		screen.blit(capa, (- 700, - 85))
		pg.draw.rect(screen, (0, 0, 0), (0, 0, 860, 45))
		screen.blit(transp, (0, 0))
		
	# Retângulo azul:		
		pg.draw.rect(barra_transp, azul_escuro_transp, barra_transp.get_rect(), 0)
		
	# Retângulo preto transparente:		
		screen.blit(barra_transp, (0, 610))

	# Títulos das músicas:
		dtext = 38 - tams_fontes[i]
		if dtext > 9:
			dtext = 9		
		screen.blit(tits[i], (10, 605 + dtext))
		
	# Barra de progresso branca:		
		pg.draw.rect(screen, branco, (10, 710, 840, 3))
		
	# Barra de progresso azul:		
		pg.draw.rect(screen, azul_escuro, (10, 710, pr - 7, 3))
		
	# Bolinha da barra de progresso:		
		pg.draw.circle(screen, azul_medio, center=(pr, 710), radius=m)
	
	# Botão de voltar ao menu:
		screen.blit(return_button, (rtx, rty))
		
	# Pause/play:		
		if not pause:
			screen.blit(pause_icon, (ppx, ppy))
		if pause:
			screen.blit(play_icon, (ppx, ppy))
	
	# Próxima/anterior:
		screen.blit(next_icon, (nx, ny))
		screen.blit(previous_icon, (pvx, pvy))
	
	# Contador de tempo:
		contador = quicksand20n.render('{:0>2d}:{:0>2d}'.format(minu, seg), True, (255, 255, 255))
		barra = quicksand20n.render('/', True, (255, 255, 255))
		screen.blit(contador, (15, 675))
		screen.blit(barra, (73, 675))
		screen.blit(dur_mus[i], (90, 675))
		pg.display.update()
	

def search_music1():
	num_mus = 0
	options = []
	dur_mus = []
	nomes_tits = []
	songs = []
	tp = []
	tams_fontes = []
	tits = []
	nums = []
	mp3s = []
	arquivos = []
	count = 0
	durf = 0

# Procurando/convertendo músicas:
	
	with os.scandir('./assets') as entries:
		for entry in entries:
			arquivos.append('./assets/' + entry.name)
			if '.mp3' in entry.name:
				count += 1
				if entry.name not in mp3s:
					mp3s.append(entry.name)
					ogg = entry.name.replace('.mp3', '.ogg')
					mp3 = '"{}"'.format(entry.name)
					ogg2 = '"{}"'.format(ogg)
					os.system(f'cd ./assets && ffmpeg -i {mp3} {ogg2}')
					songs.append('./assets/' + ogg)	 
					tp.append(40)
					name = ogg.replace('.ogg', '')
					tag = TinyTag.get('./assets/' + ogg)
					dur = int(tag.duration)
					conversion = datetime.timedelta(seconds=dur)
					durf = str(conversion)
					num_mus += 1
					nums.append(quicksand20.render(f'{num_mus}', True, (255, 255, 255)))
					dur_mus.append(quicksand20n.render(f'{durf[2:]}', True, (255, 255, 255)))
					options.append(quicksand20.render(f'|  {name}', True, (255, 255, 255)))
					print(f'{name} adicionado com sucesso!')
					tam_fonte = (1680 // len(name))
					if tam_fonte > 38:
						tam_fonte = 38
					if tam_fonte < 20:
						tam_fonte = 20
					tams_fontes.append(tam_fonte)
					quicksand38 = pg.font.SysFont("quicksand", tam_fonte)
					tits.append(quicksand38.render(f'{name}', True, (220, 220, 220)))
					os.system(f'cd ./assets && rm {mp3}')
					arquivos.remove('./assets/' + entry.name)
					arquivos.append('./assets/' + ogg)
			if '.ogg' in entry.name:
				if ('./assets/' + entry.name) not in songs:
					songs.append('./assets/' + entry.name)
					tp.append(40)
					name = entry.name.replace('.ogg', '')
					tag = TinyTag.get('./assets/' + entry.name)
					dur = int(tag.duration)
					conversion = datetime.timedelta(seconds=dur)
					durf = str(conversion)
					num_mus += 1
					nums.append(quicksand20.render(f'{num_mus}', True, (255, 255, 255)))
					dur_mus.append(quicksand20n.render(f'{durf[2:]}', True, (255, 255, 255)))
					options.append(quicksand20.render(f'|  {name}', True, (255, 255, 255)))
					print(f'{name} adicionado com sucesso!')
					tam_fonte = (1680 // len(name))
					if tam_fonte > 38:
						tam_fonte = 38
					if tam_fonte < 20:
						tam_fonte = 20
					tams_fontes.append(tam_fonte)
					quicksand38 = pg.font.SysFont("quicksand", tam_fonte)
					tits.append(quicksand38.render(f'{name}', True, (220, 220, 220)))
			elif '.ogg' not in entry.name:
				count += 1
		for x in songs:
			if x not in arquivos:
				print(x, 'removido!')
				options.pop(songs.index(x))
				tp.pop(songs.index(x))
				songs.remove(x)
				num_mus -= 1

		if len(arquivos) == count:
			songs = []
			tp = []
			lista = []
			options = []
			tits = []
			num_mus = 0
		print('nº de arquivos:', len(arquivos),'outros:', count, 'nº de músicas:', num_mus)
	return songs, nums, dur_mus, options, tp, tams_fontes, tits, num_mus

search_music1()

lista_sm1 = search_music1()
songs = lista_sm1[0]
nums = lista_sm1[1]
dur_mus = lista_sm1[2]
options = lista_sm1[3]
tp = lista_sm1[4]
tams_fontes = lista_sm1[5]
tits = lista_sm1[6]
num_mus = lista_sm1[7]

# Variáveis do menu inicial:

button_number = i = fade = q = w = count = 0
faden = 15
y = 168
yt = 160
rx = 820
ry = 122
rsize = 30
run = True
exiting = False
dim = False
is_loading = False
r_clicking = False
arquivos = []
lista = []

#---------------------------------------------- Loop do Menu Inicial --------------------------------------------------#

while run:
	mixer.init()
	mouse = pg.mouse.get_pressed(num_buttons=5)
	mx, my = pg.mouse.get_pos()
	count = 0
	arquivos = []
	rect_size = (840, 40)
	barra_azul_transp = pg.Surface(rect_size, pg.SRCALPHA)
	transps = []
	refresh = transform.scale(image.load('./assets/refresh.png'), (rsize, rsize))
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		key = pg.key.get_pressed()
		if key[pg.K_ESCAPE]:
			faden = - 20
			exit.set()
			exiting = True
		if event.type == MOUSEBUTTONDOWN:
			button_number = event.button
			if button_number == 1:
				if 820 < mx < 850 and 122 < my < 152:
					r_clicking = True
					search_music1()
					lista_sm1 = search_music1()
					songs = lista_sm1[0]
					nums = lista_sm1[1]
					dur_mus = lista_sm1[2]
					options = lista_sm1[3]
					tp = lista_sm1[4]
					tams_fontes = lista_sm1[5]
					tits = lista_sm1[6]
					num_mus = lista_sm1[7]
		if event.type == pg.MOUSEBUTTONUP:
			button_number = event.button
			if button_number == 1:
				r_clicking = False			

			# Clicando nas opções de música:
	
				if 30 < mx < 830:
					for c in range(0, len(tp)):
						if lista == []:
							lista.append(list(range((yt + (c * 42)), (yt + 42 + (c * 42)))))
						elif lista != [] and list(range((yt + (c * 42)), (yt + 42 + (c * 42)))) not in lista:
							lista.append(list(range((yt + (c * 42)), (yt + 42 + (c * 42)))))
						if (my + (w * 25)) in lista[c]:
							i = c
							is_loading = True
							if is_loading:
								pg.draw.rect(barra_azul_transp, (0, 30, 180, 220), barra_azul_transp.get_rect(), 20, border_radius=5)
								screen.blit(barra_azul_transp, (10, yt + (i * 42)))
								pg.draw.rect(screen, (0, 0, 0), (60, (yt + 8 + (i * 42)), 150, 25), border_radius=12)
								screen.blit(loading, (75, yt + 5 + (c * 42)))
								pg.display.update()
							p = t = fade = 0
							mixer.music.load(songs[c])
							mixer.music.play()
							playing(i)
							tp[c] = 40
							is_loading = False
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
					
# Passando o mouse por cima das opções:

	if len(tp) != 0:
		for c in range(0, len(tp)):
			if lista == []:
				lista.append(list(range((yt + (c * 42)), (yt + 42 + (c * 42)))))
			elif lista != [] and list(range((yt + (c * 42)), (yt + 42 + (c * 42)))) not in lista:
				lista.append(list(range((yt + (c * 42)), (yt + 42 + (c * 42)))))
		if 10 < mx < 850:
			if 0 < my < 720:
				for z in range(0, len(tp)):
					if (my + (w * 25)) not in lista[z]:
						tp[z] = 40
					else:
						tp[z] = 180
		if my < 160 or my > 718 or mx > 850 or 10 > mx:
			for c in range(0, len(tp)):
				tp[c] = 40
			exit.wait(0.01)
	if 820 < mx < 850 and 122 < my < 152:
		if not r_clicking:
			rx = 817
			ry = 119
			rsize = 33
		else:
			rsize = 34
			rx = 816
			ry = 118
	else:
		rx = 820
		ry = 122
		rsize = 30
		
	fade += faden
	if fade > 100:
		fade = 100
	if fade < 0 and exiting:
		run = False
	screen.fill((0, 0, 10))
	back.set_alpha(fade)
	screen.blit(back, (0, 0))
	if not exiting:
		back2.set_alpha(100)
		for k in range(0, len(tp)):
			pg.draw.rect(barra_azul_transp, (0, 30, 120, tp[k]), barra_azul_transp.get_rect(), 20, border_radius=5)
			transps.append(barra_azul_transp)
			screen.blit(transps[k], (10, yt + (k * 42)))
		for k in range(0, len(tp)):
			screen.blit(nums[k], (20, y + (k * 42)))
			screen.blit(options[k], (50, y + (k * 42)))
			screen.blit(dur_mus[k], (765, y + (k * 42)))
		screen.blit(back2, (-100, - 410))
		screen.blit(player3, (125, 26))
		screen.blit(player2, (124, 25))		
		screen.blit(player, (123, 20))
		screen.blit(author, (585, 110))
		screen.blit(refresh, (rx, ry))
	elif exiting:
		screen.blit(player3, (125, 306))
		screen.blit(player2, (124, 305))
		screen.blit(player, (123, 300))
	display.update()
pg.quit()


