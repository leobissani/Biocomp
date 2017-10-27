import os

os.system("cls")

print '\t\t  DESAFIO COMPUTACIONAL III'
print '\t\t\t  MENU'
print '\tAlinhamento de Sequencias (Smith-Waterman)'
# LEITURA DE SEQUENCIAS
seq1 = raw_input("Insira a sequencia 1: _\b")
seq2 = raw_input("Insira a sequencia 2: _\b")
seq1 = seq1.upper()
seq2 = seq2.upper()

print "\nSequencias inseridas:"
for i in range(len(seq1)):
	print seq1[i],
print
for i in range(len(seq2)):
	print seq2[i],

tamSeq1 = len(seq1)
tamSeq2 = len(seq2)
matrizFinal = [0]*(tamSeq1 + 1)

# MATRIZ DE MERITO
# Cria a matriz com o tamanho das sequencias (tamSeq1 x tamSeq2)
for i in range(len(matrizFinal)):
	matrizFinal[i] = [0]*(tamSeq2 + 1)

matriz = []
path = []
maior = []
posicao = []
proximo = 0
posicaoMaior = []
dicPosFinal = {}
vetorFinal = []
vetorComparador = []
linha = (tamSeq2) 
coluna = (tamSeq1)
tamSeq1 = " " + seq2
tamSeq2 = " " + seq1

for i in range(linha + 1):
	matriz.append([0]*(coluna + 1))
	path.append(["N"]*(coluna + 1))

# Imprime a matriz na tela
def imprimeMatriz(matrizFinal):
	print '\t' + ('\t'.join(map(str,list(tamSeq1))))
	i = 0
	for line in matrizFinal:
		print tamSeq2[i] + "\t" + ('\t'.join(map(str,line)))
		i += 1

# Pontua as posicoes da matriz conforme as regras dadas
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            Sij = [matrizFinal[i][j] + 1, matrizFinal[i-1][j] - 2, matrizFinal[i][j-1] - 2, 0]
            matrizFinal[i+1][j+1] = max(Sij)
        if seq1[i] != seq2[j]:
            Sij = [matrizFinal[i][j] - 1, matrizFinal[i-1][j] - 2, matrizFinal[i][j-1] - 2, 0]
            matrizFinal[i+1][j+1] = max(Sij)

print "\n\nMatriz:"
imprimeMatriz(matrizFinal)

# TRACEBACK
# Encontra o maior valor dentro de toda a matriz
for i in range(len(matrizFinal)):
	maior.append(max(matrizFinal[i]))
for i in range(len(maior)):
	maiorValor = max(maior)

# Encontra a posicao do maior valor, para iniciar o traceback
def encontraPosicaoMaior(matrizFinal, maiorValor):
	posInterna = []
	pos = []
	counter = 0

	i = len(matrizFinal) - 1
	j = len(matrizFinal) - 1

	# Varre a matriz de cima para baixo, da direita para a esquerda
	while i > 0:
		while j > 0:
			if matrizFinal[i][j] == maiorValor and counter == 0:
				pos = [i, j] # vetor que guarda posicao do maior valor
				posInterna.append(pos) # lista que guarda os vetores de posicao
				counter += 1
			# if counter > 0:
			# 	flagMais = 1
			j -= 1
		i -= 1
		j = len(matrizFinal) - 1

	return posInterna

posicaoMaior = encontraPosicaoMaior(matrizFinal, maiorValor)

print "\nTraceback:"
print maiorValor, posicaoMaior
dicPosFinal[maiorValor] = posicaoMaior
vetorFinal.append(posicaoMaior[0])

# Varre as posicoes ao redor do maior valor, para buscar o proximo valor
def encontraProximoValor(matrizFinal, maiorValor, posicaoMaior):
	arredores = [matrizFinal[(posicaoMaior[0][0])-1][(posicaoMaior[0][1])-1], 
	matrizFinal[(posicaoMaior[0][0])-1][(posicaoMaior[0][1])],
	matrizFinal[(posicaoMaior[0][0])][(posicaoMaior[0][1])-1]]

	indice = 3
	maior = 0

	maior = max(arredores)

	return maior

# Funcao que encontra as coordenadas do valor de entrada "proximo" (no caso, maior valor nas redondezas do valor anterior) na matriz
def encontraPosicaoProximo(matrizFinal, proximo, posicaoMaior):
	posInterna = posicaoMaior
	posFinal = []
	pos = []
	counter = 0

	i = len(matrizFinal) - 1
	j = len(matrizFinal) - 1

	# Varre a matriz de cima para baixo, da direita para a esquerda
	while i > 0:
		while j > 0:
			if matrizFinal[i][j] == proximo and ((i == (posInterna[0][0])-1) or i == (posInterna[0][0])) and ((j == (posInterna[0][1])-1) or j == (posInterna[0][1])):
				pos = [i, j] # vetor que guarda posicao do maior valor
				posFinal.append(pos) # lista que guarda os vetores de posicao
				counter += 1
			# if counter > 0:
			# 	flagMais = 1
			j -= 1
		i -= 1
		j = len(matrizFinal) - 1

	return posFinal

proximo = encontraProximoValor(matrizFinal, maiorValor, posicaoMaior)
proxPosic = encontraPosicaoProximo(matrizFinal, proximo, posicaoMaior)
dicPosFinal[proximo] = proxPosic
vetorFinal.append(proxPosic[0])
print proximo, proxPosic

while proximo > 0:
	proximo = encontraProximoValor(matrizFinal, proximo, proxPosic)
	proxPosic = encontraPosicaoProximo(matrizFinal, proximo, proxPosic)
	if proximo == 0:
		break
	if len(proxPosic) <= 0:
		break
	if len(proxPosic) >= 2:
		proxPosic[0] = proxPosic[1]
	dicPosFinal[proximo] = proxPosic
	vetorFinal.append(proxPosic[0])
	print proximo, proxPosic

print

# ALINHAMENTO
print "Alinhamento:"
seq1Final = []
seq2Final = []
indEx = 0
indIn = 0

# Percorre o vetor final que guarda as posicoes do traceback e faz o calculo para ver se andou na diagonal, esquerda ou para  cima
# dando assim o alinhamento para as sequencias
seq1Final.append(seq1[(vetorFinal[indEx][indIn])-1])
seq2Final.append(seq1[(vetorFinal[indEx][indIn])-1])

for i in range((len(vetorFinal))-1):
	if vetorFinal[indEx][indIn] == vetorFinal[indEx+1][indIn] and vetorFinal[indEx][indIn+1] != vetorFinal[indEx+1][indIn+1]:
		seq2Final.append("-")
		seq1Final.append(seq1[(vetorFinal[indEx][indIn])-2])
	if vetorFinal[indEx][indIn] != vetorFinal[indEx+1][indIn] and vetorFinal[indEx][indIn+1] == vetorFinal[indEx+1][indIn+1]:
		seq1Final.append("-")
		seq2Final.append(seq1[(vetorFinal[indEx][indIn])-2])
	if vetorFinal[indEx][indIn] != vetorFinal[indEx+1][indIn] and vetorFinal[indEx][indIn+1] != vetorFinal[indEx+1][indIn+1]:
		seq1Final.append(seq1[(vetorFinal[indEx][indIn])-2])
		seq2Final.append(seq1[(vetorFinal[indEx][indIn])-2])
	indEx += 1

seq1Final = seq1Final[::-1]
seq2Final = seq2Final[::-1]

print "Sequencia 1: " + str(seq1Final)
print "Sequencia 2: " + str(seq2Final)
print