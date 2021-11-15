import random as rd

def gerarMapa(celulasX,celulasY,porcentagemPreenchido):
	mapa = [[0 if (rd.randint(1,100) < porcentagemPreenchido or i == 0 or i == celulasY-1 or j == 0 or j == celulasX-1 ) else 1 for i in range(celulasY)] for j in range(celulasX)]
	return mapa

def alisarMapa(mapa,qntIteracoes):
	for i in range(qntIteracoes):
		mapaCopia = [[0 for i in range(len(mapa[0]))] for j in range(len(mapa))]
		for x in range(1,len(mapa)-1):
			for y in range(1,len(mapa[0])-1):
				quantVizinhos = contarVizinhos(mapa,x,y)
				if mapa[x][y] == 0:
					if quantVizinhos < 4:
						mapaCopia[x][y] = 1
				else:
					if quantVizinhos > 4:
						mapaCopia[x][y] = 0
					else:
						mapaCopia[x][y] = 1
		mapa = mapaCopia
	return mapa

def contarVizinhos(mapa,x,y):
	contador = 0
	for indexX in range(x-1,x+2):
		for indexY in range(y-1,y+2):
			if indexX < 0 or indexX > len(mapa)-1 or indexY < 0 or indexY > len(mapa[0])-1:
				contador += 0
			else:
				if indexX == x and indexY == y:
					continue
				elif mapa[indexX][indexY] == 0:
					contador += 1

	return contador