import os

os.system("cls")

print '\t\t  DESAFIO COMPUTACIONAL IV'
print '\t\t\t  MENU'
print '\tConstrucao de Arvores Filogeneticas Neighbor-Joining Method'

# CRIACAO DA MATRIZ
matriz = [[0, 0.1890, 0.1100, 0.1130, 0.2150],[0.1890, 0, 0.1790, 0.1920, 0.2110],[0.1100, 0.1790, 0, 0.09405, 0.2050],[0.1130, 0.1920, 0.0940, 0, 0.2140],[0.2150, 0.2110, 0.2050, 0.2140, 0]]
newMatriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
gorila, orangotango, humano, chimpanze, gibao = 0, 0, 0, 0, 0
posGorila = 0
posOrangotango = 1
posHumano = 2
posChimpanze = 3
posGibao = 4
n = len(matriz)

# PASSO 1
def calculaDistanciaTotal(matriz, posicao):
	distancia = 0

	for i in range(len(matriz)):
		distancia = distancia + matriz[posicao][i]

	return distancia

def calculaDistancia(matriz, posEntrada, posSaida):
	distancia = 0

	distancia = matriz[posEntrada][0] - matriz[posSaida][0]
	if distancia < 0:
		distancia = distancia * (-1)

	return distancia

gorila = calculaDistanciaTotal(matriz, posGorila)
orangotango = calculaDistanciaTotal(matriz, posOrangotango)
humano = calculaDistanciaTotal(matriz, posHumano)
chimpanze = calculaDistanciaTotal(matriz, posChimpanze)
gibao = calculaDistanciaTotal(matriz, posGibao)

distGorilaOrango = calculaDistancia(matriz, posGorila, posOrangotango)
distGorilaHumano = calculaDistancia(matriz, posGorila, posHumano)
distGorilaChimpanze = calculaDistancia(matriz, posGorila, posChimpanze)
distGorilaGibao = calculaDistancia(matriz, posGorila, posGibao)
distOrangoHumano = calculaDistancia(matriz, posOrangotango, posHumano)
distOrangoChimpanze = calculaDistancia(matriz, posOrangotango, posChimpanze)
distOrangoGibao = calculaDistancia(matriz, posOrangotango, posGibao)
distHumanoChimpanze = calculaDistancia(matriz, posHumano, posChimpanze)
distHumanoGibao = calculaDistancia(matriz, posHumano, posGibao)
distChimpanzeGibao = calculaDistancia(matriz, posChimpanze, posGibao)

for i in range(len(matriz)):
	for j in range(len(matriz)):
		if (i == posGorila and j == posOrangotango) or (i == posOrangotango and j == posGorila):
			newMatriz[i][j] = (n-2)*distGorilaOrango - gorila - orangotango
		if (i == posGorila and j == posHumano) or (i == posHumano and j == posGorila):
			newMatriz[i][j] = (n-2)*distGorilaHumano - gorila - humano
		if (i == posGorila and j == posChimpanze) or (i == posChimpanze and j == posGorila):
			newMatriz[i][j] = (n-2)*distGorilaChimpanze - gorila - chimpanze
		if (i == posGorila and j == posGibao) or (i == posGibao and j == posGorila):
			newMatriz[i][j] = (n-2)*distGorilaGibao - gorila - gibao
		if (i == posOrangotango and j == posHumano) or (i == posHumano and j == posOrangotango):
			newMatriz[i][j] = (n-2)*distOrangoHumano - orangotango - humano
		if (i == posOrangotango and j == posChimpanze) or (i == posChimpanze and j == posOrangotango):
			newMatriz[i][j] = (n-2)*distOrangoChimpanze - orangotango - chimpanze
		if (i == posOrangotango and j == posGibao) or (i == posGibao and j == posOrangotango):
			newMatriz[i][j] = (n-2)*distOrangoGibao - orangotango - gibao
		if (i == posHumano and j == posChimpanze) or (i == posChimpanze and j == posHumano):
			newMatriz[i][j] = (n-2)*distHumanoChimpanze - humano - chimpanze
		if (i == posHumano and j == posGibao) or (i == posGibao and j == posHumano):
			newMatriz[i][j] = (n-2)*distHumanoGibao - humano - gibao
		if (i == posChimpanze and j == posGibao) or (i == posGibao and j == posChimpanze):
			newMatriz[i][j] = (n-2)*distChimpanzeGibao - chimpanze - gibao

print newMatriz

# PASSO 2

menorLista = []

def encontraMenor(matriz):
	menor = []

	for i in range(len(matriz)):
		menor.append(min(newMatriz[i]))
		print menor

	return menor

menorLista = encontraMenor(matriz)
print menorLista

# PASSO 3

variacao = (gorila - orangotango)/(n-2)
print variacao

distanciaGorilaOrango = (gorila + variacao)/2
distanciaOrangoGorila = (orangotango - variacao)/2

print distanciaGorilaOrango
print distanciaOrangoGorila