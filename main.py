import pygame
import random as rd
import mapa as mp
import timeit

pygame.init()
pygame.display.set_caption('A* pathfinding')

width = 500
height = 500
celulasX = 120
celulasY = 100

tamanhoCelulaX = width//celulasX
tamanhoCelulaY = height//celulasY
width = tamanhoCelulaX*celulasX
height = tamanhoCelulaY*celulasY

screen = pygame.display.set_mode([width, height])
running = True
porcentagemPreenchido = 45
mapa = mp.gerarMapa(celulasX,celulasY,porcentagemPreenchido)

while running:
	comecoTempo = timeit.default_timer()
	screen.fill((255, 255, 255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		click = pygame.mouse.get_pressed()
		if click[0]:
			mapa = mp.gerarMapa(celulasX,celulasY,porcentagemPreenchido)
	
	for x in range(len(mapa)):
		for y in range(len(mapa[0])):
			if mapa[x][y] == 0:
				pygame.draw.rect(screen, (0,0,0), (x*tamanhoCelulaX, y*tamanhoCelulaY, tamanhoCelulaX,tamanhoCelulaY))

	pygame.display.flip()
	mapa = mp.alisarMapa(mapa,1)
	fimTempo = timeit.default_timer()
	print('Tempo: ', fimTempo - comecoTempo)



pygame.quit()


