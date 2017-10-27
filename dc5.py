import os
import collections

os.system("cls")

print '\t\t  DESAFIO COMPUTACIONAL V'
print '\t\t\t  MENU'
print '\tBusca por Padroes - Motivos em Sequencias\n'
print 'A - Sequencia A: n = 5000, m = 4, l = 7'
print 'B - Sequencia A: n = 4000, m = 3'
opcao = raw_input("Insira uma opcao: _\b")

t = 0			# numero de sequencias de DNA
mutacoes = 0	# numero maximo de mutacoes
n = 0			# tamanho de cada sequencia de DNA
lmer = 0		# tamanho do motivo  (l-mer)
posInicio = 0	# posicao de inicio de um l-mer em uma sequencia i
vetorS = []		# vetor com as posicoes de inicio de cada motivo
sequencias = ""	# recebe o arquivo
motif = ""

# FUNCOES
def leArquivo():
	conteudoFinal = ""

	varFile = open("seq.txt","r")	# abre o arquivo em modo leitura
	# ignoreLine = varFile.readline() # ignora o conteudo da primeira linha

	while True:
		conteudo = varFile.readline() # guarda o conteudo do arquivo linha por linha
		if conteudo == '':
			break
		conteudoFinal += conteudo # passa o conteudo para uma string

	conteudoFinal = conteudoFinal.replace("\n","") # remove os \n da string

	return conteudoFinal

def criaMatriz(lmer, qtsSeq, matrizPt):
	limite = 4

	for i in range(limite):
		linha = []
		for j in range(lmer):
			linha = linha + [0]
		matrizPt = matrizPt + [linha]

	return matrizPt

def separaSequencias(checkPoint, sequencias, n):
	sequenciasSeparadas = ""

	for i in range(n):
		sequenciasSeparadas += sequencias[checkPoint]
		checkPoint += 1

	return sequenciasSeparadas

def contaSequencias(sequencias, n):
	numSequencias = 0
	tamFile = len(sequencias)

	numSequencias = tamFile / n

	return numSequencias

def contaLmers(listSequencias, lmer, n):
	contaLmers = 0

	for i in range(n):
		if len(str(listSequencias[0][i: i + lmer])) >= lmer:	# apenas considera os codons de tamanho desejado
			contaLmers += 1	# incrementa o contador de codons
			i += 1	# incrementa o contador interno

	# print "Lista de todos os possiveis lmers de cada sequencia: " + str(contaLmers)

	return contaLmers

def comparaSequencias(listSequencias, lmer, posSeq1, posSeq2, match, lmersNro, checkPoint, extPos1, extPos2):
	seq1 = ""
	seq2 = ""
	i = extPos1
	j = extPos2

	seq1 = listSequencias[i][posSeq1 : posSeq1 + lmer]
	seq2 = listSequencias[j][posSeq2 : posSeq2 + lmer]

	return seq1, seq2

def pontuaMatrizSequencias(sequenciasTemporarias, extPos1, extPos2, posSeq1, posSeq2, index1, matrizPt):

	if (sequenciasTemporarias[extPos1][index1] == sequenciasTemporarias[extPos2][index1]) and (sequenciasTemporarias[extPos1][index1] == "A"):
		matrizPt[0][index1] += 1
	if (sequenciasTemporarias[extPos1][index1] == sequenciasTemporarias[extPos2][index1]) and (sequenciasTemporarias[extPos1][index1] == "C"):
		matrizPt[1][index1] += 1
	if (sequenciasTemporarias[extPos1][index1] == sequenciasTemporarias[extPos2][index1]) and (sequenciasTemporarias[extPos1][index1] == "G"):
		matrizPt[2][index1] += 1
	if (sequenciasTemporarias[extPos1][index1] == sequenciasTemporarias[extPos2][index1]) and (sequenciasTemporarias[extPos1][index1] == "T"):
		matrizPt[3][index1] += 1

	return matrizPt

def	pontuaMatriz(listSequencias, lmersNro, lmer, matrizPt, checkPoint):
	internal = checkPoint
	
	for i in range(len(listSequencias)):
		if (listSequencias[i][internal] == "A"): matrizPt[0][internal] += 1
		if (listSequencias[i][internal] == "C"): matrizPt[1][internal] += 1
		if (listSequencias[i][internal] == "G"): matrizPt[2][internal] += 1
		if (listSequencias[i][internal] == "T"): matrizPt[3][internal] += 1

	return matrizPt

def arranjaColunas(matrizPt, lmer, listScore):

	for i in range(lmer):
		linha = []
		for j in range(len(matrizPt)):
			linha = linha + [matrizPt[j][i]]
		listScore = listScore + [linha]

	return listScore

def maiorValor(listScore):
	maior = []
	scoreTemporario = 0

	for i in range(len(listScore)):
		maior.append(max(listScore[i]))
		scoreTemporario += maior[i]
	
	return scoreTemporario, maior

def calculaScore(maior, scoreFinal):

	for i in range(len(maior)):
		scoreFinal += maior[i]

	return scoreFinal


# INICIO DO PROGRAMA
sequencias = leArquivo()

if opcao == 'A' or opcao == 'a':
	n = 70
	checkPoint = 0
	match = 0
	mutacoes = 4
	lmer = 7
	lmersNro = 0
	limitSeq = 0
	posSeq1 = 0
	posSeq2 = 0
	listSequencias = []
	sequenciasTemporarias = []
	matrizPt = []
	listScore = []
	resultVetor = []
	maior = []
	scoreFinal = 0
	listScoreFinal = []
	extPos1 = 0
	extPos2 = 1
	index1 = 0
	eight = 8
	posicaoSMotif = 0
	vetorScoreFinal = {}

	qtsSeq = contaSequencias(sequencias, n)	# conta o numero de sequencias do arquivo

	for i in range(qtsSeq):
		listSequencias.append(separaSequencias(checkPoint, sequencias, n))	# separa as sequencias em uma lista
		checkPoint += n

	matrizPt = criaMatriz(lmer, qtsSeq, matrizPt)	# cria uma matriz de pontuacao

	lmersNro = contaLmers(listSequencias, lmer, n)	# conta os possiveis lmers existentes na sequencia
	checkPoint = 0

	# compara as sequencias
	for i in range(lmersNro):
		posSeq1 = 0
		index1 = 0
		for j in range(lmersNro):
			for k in range(eight):
				sequenciasTemporarias = comparaSequencias(listSequencias, lmer, posSeq1, posSeq2, match, lmersNro, checkPoint, extPos1, extPos2)
				matrizPt = pontuaMatrizSequencias(sequenciasTemporarias, extPos1, extPos2, posSeq1, posSeq2, index1, matrizPt)
				index1 += 1
				if index1 >= 7:
					listScore = arranjaColunas(matrizPt, lmer, listScore)	# arranja as colunas em listas para encontrar o maior valor de cada coluna
					resultVetor = maiorValor(listScore)
					maior = resultVetor[1]
					posicaoSMotif += 1
					if posicaoSMotif <= n:
						scoreFinal = calculaScore(maior, scoreFinal)
						vetorScoreFinal[posicaoSMotif] = scoreFinal
					scoreFinal = 0
					listScore = []
					matrizPt = []
					matrizPt = criaMatriz(lmer, qtsSeq, matrizPt)	# cria uma matriz de pontuacao
					index1 = 0
					maior = 0
			posSeq1 += 1
		posSeq2 += 1

	print "Pontuacao de cada posicao da sequencia:" 
	print vetorScoreFinal

	match = max(vetorScoreFinal, key=vetorScoreFinal.get) # encontra em que posicao esta o maior valor na sequencia

	print "Motif Encontrado: " + str(listSequencias[0][match: match + lmer]) + " (posicao " + str(match) + ")"
