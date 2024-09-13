#!/usr/bin/env python3

# Bibliotecas/Verificação de bibliotecas:
import os
from tinytag import TinyTag
from threading import Event
import time
import datetime
import pygame as pg
from pygame import mixer, image, display, transform
from pygame.locals import *
from definitions import Fonts as fonts

# Iniciando o pygame:
pg.init()
exit = Event()
screen = display.set_mode((860, 720))

# Imagens:
back = transform.scale(image.load('./assets/back.jpg'), (860, 720))
back2 = transform.scale(image.load('./assets/back.jpg'), (1060, 559))
player_icon = transform.scale(image.load('./assets/player_back.jpg'), (100, 100))

# Textos do Menu Inicial:
display.set_caption('NEO PLAYER')
display.set_icon(player_icon)
player = fonts.quicksand80.render('{ NEO PLAYER }', True, (220, 220, 220))
player3 = fonts.quicksand80.render('{ NEO PLAYER }', True, (0, 0, 180))
player2 = fonts.quicksand80.render('{ NEO PLAYER }', True, (0, 0, 0))
author = fonts.quicksand16.render('by $Neo', True, (255, 255, 255))
loading = fonts.quicksand22b.render('Loading . . .', True, (0, 250, 0))
loading2 = fonts.quicksand22b.render('Loading . . .', True, (0, 0, 0))
capa = transform.scale(image.load('./assets/player_back.jpg'), (1720, 720))


# Função "música tocando"
def playing(i):
	v = 1
	color_change = n = 0
	img_alpha_change = 1
	m = 0
	z = 10
	
	play_pause_x = 395
	play_pause_y = 655
	play_pause_size = 50
	
	next_x = 455
	next_y = 665
	next_size = 32
	
	previous_x = 350
	previous_y = 665
	previous_size = 32
	
	is_playrun = True
	is_clicking = False
	is_nclicking = False
	is_pclicking = False
	is_pause = False
	
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
	
	while is_playrun:
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
			play_pause_x = 394
			play_pause_y = 654
			play_pause_size = 52
		else:
			play_pause_x = 395
			play_pause_y = 655
			play_pause_size = 50
		play_icon = transform.scale(image.load('./assets/play.png'), (play_pause_size, play_pause_size))
		pause_icon = transform.scale(image.load('./assets/pause.png'), (play_pause_size, play_pause_size))
		previous_icon = transform.scale(image.load('./assets/previous.png'), (next_size, next_size))
		
	# Mouse sobre o botão next:
		if 453 < mx1 < 487 and 663 < my1 < 697 and not is_nclicking:
			next_x = 454
			next_y = 664
			next_size = 35
		else:
			next_x = 455
			next_y = 665
			next_size = 32
		next_icon = transform.scale(image.load('./assets/next.png'), (next_size, next_size))
		
	# Mouse sobre o botão previous:
		if 349 < mx1 < 383 and 663 < my1 < 697 and not is_pclicking:
			previous_x = 349
			previous_y = 664
			previous_size = 35
		else:
			previous_x = 350
			previous_y = 665
			previous_size = 32
		previous_icon = transform.scale(image.load('./assets/previous.png'), (previous_size, previous_size))			
			
	# Mouse sobre a bolinha azul:
		if pr - 20 < mx1 < pr + 20 and 698 < my1 < 720:
			m = 7
		else:
			m = 0
		for event1 in pg.event.get():
			if event1.type == pg.QUIT:
				is_playrun = False
			if event1.type == MOUSEBUTTONDOWN:
				button_number1 = event1.button
				if button_number1 == 1:
				
				# Clicando...
				# no botão de return:
					if 10 < mx1 < 40 and 10 < my1 < 40:
						mixer.music.stop()
						is_pause = True
						is_playrun = False
						
				# na bolinha azul:
					if pr - 15 < mx1 < pr + 15 and 705 < my1 < 720:
						m = 8
						is_clicking = True
							
				# na barra de progresso:
					elif pr + 15 < mx1 < 850 or 10 < mx1 < pr - 15:
						if 705 < my1 < 720:
							is_clicking = True
						
				# no play/pause:
					if 394 < mx1 < 449 and 654 < my1 < 708 and pr >= 849 and not is_clicking:
						mixer.music.stop()
						mixer.music.play()
						pr = 50
						nn = 0
						is_pause = False
					elif 394 < mx1 < 449 and 654 < my1 < 708 and pr < 849:
						ppclicking = True
							
				# no botão next:
					if 453 < mx1 < 485 and 663 < my1 < 697:
						is_nclicking = True
				
				# no botão previous:
					if 349 < mx1 < 383 and 663 < my1 < 697:
						is_pclicking = True		
							
		# Soltando o clique:
			if event1.type == MOUSEBUTTONUP:
				button_number1 = event1.button
				if color_change >= 80 and button_number1 == 1 and is_clicking:
					is_clicking = False
					prt = pr - 14
					if pr <= 10:
						pr = 10
						mixer.music.play()
						is_pause = False
					if pr >= 849:
						mixer.music.stop()
						pr = 849
						is_pause = True
					if mx1 <= 10: 	
						pr = 10
						n = 0
					if 10 < mx1 < 849:
						d = 840 / s
						n = prt / d
						nn = n - mus_pos
						mixer.music.set_pos(n)
						pr = mx1 - 4
						is_pause = False
				elif ppclicking and pr < 849:
					ppclicking = False
					if not is_pause:
						mixer.music.pause()
						is_pause = True
					elif is_pause:
						mixer.music.unpause()
						mixer.music.set_pos(mus_pos)
						is_pause = False
				elif is_nclicking:
					is_nclicking = False
					pr -= pr
					mixer.music.unload()
					mixer.quit()
					i += 1
					if i >= len(songs):
						i = 0
					is_playrun = False
					playing(i)
				elif is_pclicking:
					pr -= pr
					mixer.music.unload()
					mixer.quit()
					i -= 1
					if i < 0:
						i = len(songs) - 1
					is_playrun = False
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
							is_pause = True
							pr = 850
						n += 5
						pr += divi * 5
						mixer.music.play(i, n)
				if key1[pg.K_LEFT]:
					is_pause = False
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
					is_pause = True
				if not is_pause:
					if key1[pg.K_SPACE]:
						if pr >= 850:
							mixer.music.rewind()
							pr = 10
							is_pause = False
						else:
							mixer.music.pause()
							is_pause = True
				elif is_pause:
					if key1[pg.K_SPACE]:
						mixer.music.unpause()
						is_pause = False
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
			play_pause_size = 50
			play_pause_x = 395
			play_pause_y = 655
		if is_nclicking:
			next_x = 455
			next_y = 665
			next_size = 32
		if is_pclicking:
			previous_x = 350
			previous_y = 665
			previous_size = 32			
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
		if is_clicking:	
			pr = mx1 - 4		
			m = 8
			if pr > 850:
				pr = 850
			elif pr < 10:
				pr = 10
		elif not is_clicking and not is_pause:
			pr = ((mus_pos + nn) * d) + 10
			if pr < 10:
				pr = 10
				mixer.music.stop()
				mixer.music.play()
		if pr > 849:
			pr = 849
			is_pause = True
			mixer.music.stop()
			
	# Variações de transparência:
		color_change += z
		img_alpha_change += 3.5 * z
		if img_alpha_change > 255:
			img_alpha_change = 255
		if img_alpha_change <= 0:
			is_playrun = False
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
		volume = fonts.quicksand20.render(f'Volume {int(v * 100)}%', True, (color_change * 3, color_change * 3, color_change * 3))
		azul_escuro = (0, 0, color_change * 1.8)
		azul_medio = (0, 0, color_change * 2)
		preto_transp = (0, 0, 0, color_change * 1.5)
		azul_escuro_transp = (0, 0, 50, color_change * 2.5)
		screen.fill((0, 0, 0))
	
	# Retângulo grande preto transparente:		
		pg.draw.rect(transp, azul_escuro_transp, transp.get_rect(), 0)
		
	# Capas dos álbuns:
		capa.set_alpha(img_alpha_change)
		screen.blit(capa, (- 700, 0))
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
		if not is_pause:
			screen.blit(pause_icon, (play_pause_x, play_pause_y))
		if is_pause:
			screen.blit(play_icon, (play_pause_x, play_pause_y))
	
	# Próxima/anterior:
		screen.blit(next_icon, (next_x, next_y))
		screen.blit(previous_icon, (previous_x, previous_y))
	
	# Contador de tempo:
		contador = fonts.quicksand20n.render('{:0>2d}:{:0>2d}'.format(minu, seg), True, (255, 255, 255))
		barra = fonts.quicksand20n.render('/', True, (255, 255, 255))
		screen.blit(contador, (15, 675))
		screen.blit(barra, (73, 675))
		screen.blit(dur_mus[i], (90, 675))
		pg.display.update()
	
# Variáveis do menu inicial:
options = []
dur_mus = []
nomes_tits = []
songs = []
tp = []
tams_fontes = []
tits = []
nums = []
mp3s = []
button_number = i = fade = q = w = count = num_mus = durf = count = 0
faden = 15
y = 168
yt = 160
run = True
exiting = False
dim = False
is_loading = False
lista = []

#---------------------------------------------- Loop do Menu Inicial --------------------------------------------------#
while run:
	mixer.init()
	mouse = pg.mouse.get_pressed(num_buttons=5)
	mx, my = pg.mouse.get_pos()
	count = 0
	rect_size = (840, 40)
	barra_azul_transp = pg.Surface(rect_size, pg.SRCALPHA)
	transps = []
	arquivos = []

# Procurando/convertendo músicas:
	with os.scandir('./assets') as entries:
		for entry in entries:
			if entry.name not in arquivos:
				arquivos.append('./assets/' + entry.name)
			if '.mp3' in entry.name:
				count += 1
				if entry.name not in mp3s:
					mp3s.append(entry.name)
					converting = fonts.quicksand16.render(f'Converting {entry.name}...', True, (255, 255, 255))
					screen.blit(converting, (10, 140))
					pg.display.update()
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
					nums.append(fonts.quicksand20.render(f'{num_mus}', True, (255, 255, 255)))
					dur_mus.append(fonts.quicksand20.render(f'  {durf[2:]}', True, (255, 255, 255)))
					options.append(fonts.quicksand20n.render(f'|   {name}', True, (255, 255, 255)))
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
					time.sleep(0.05)
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
					nums.append(fonts.quicksand20.render(f'{num_mus}', True, (255, 255, 255)))
					dur_mus.append(fonts.quicksand20.render(f'  {durf[2:]}', True, (255, 255, 255)))
					options.append(fonts.quicksand20n.render(f'|   {name}', True, (255, 255, 255)))
					print(f'{name} adicionado com sucesso!')
					tam_fonte = (1680 // len(name))
					if tam_fonte > 38:
						tam_fonte = 38
					if tam_fonte < 20:
						tam_fonte = 20
					tams_fontes.append(tam_fonte)
					quicksand38 = pg.font.SysFont("quicksand", tam_fonte)
					tits.append(quicksand38.render(f'{name}', True, (220, 220, 220)))
					time.sleep(0.05)
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
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			run = False
		key = pg.key.get_pressed()
		if key[pg.K_ESCAPE]:
			faden = - 20
			exit.set()
			exiting = True

		if event.type == pg.MOUSEBUTTONUP:
			button_number = event.button
			if button_number == 1:

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
								pg.draw.rect(barra_azul_transp, (0, 30, 255, 255), barra_azul_transp.get_rect(), 20, border_radius=5)
								screen.blit(barra_azul_transp, (10, yt + (i * 42)))
								screen.blit(loading2, (52.5, yt + 7.5 + (c * 42)))
								screen.blit(loading, (50, yt + 5 + (c * 42)))
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
	elif exiting:
		screen.blit(player3, (125, 306))
		screen.blit(player2, (124, 305))
		screen.blit(player, (123, 300))
	display.update()
pg.quit()

