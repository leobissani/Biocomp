			 ### DESAFIO COMPUTACIONAL I ###
			### Leonardo Bissani - 220485 ###

import collections

print "DESAFIO COMPUTACIONAL I - MENU"
fileName = raw_input("Insira o nome do arquivo: _\b")

var_file = open(fileName,"r")	# abre o arquivo em modo leitura
dadoIgnore = var_file.readline() # ignora o conteudo da primeira linha

contaCodons = 0		# contador de codons
codonsList = []		# inicializa a lista que guardara as possibilidades de codons
conteudoFinal = ""	# inicializa a variavel que vai guardar o conteudo do arquivo

while True:
	conteudo = var_file.readline() # guarda o conteudo do arquivo linha por linha
	if conteudo == '':
		break
	conteudoFinal += conteudo # passa o conteudo para uma string

conteudoFinal = conteudoFinal.replace("\n","") # remove os \n da string

# apresentacao do menu
print "DESAFIO COMPUTACIONAL I - MENU"
print "A) Quantidade diferente de codons de tamanho 5 presentes em W"
print "B) Quantidade de subsequencias separadas por X (TTT) em W"
print "C) Quantidade de subsequencias do tipo sUsUs presentes em W"
print "D) Quantidade de palindromos diferentes de tamanho 7 presentes em W"
print "E) Principais frames obtidos a partir da sequencia de nucleotideos"
opcao = raw_input("Insira uma opcao: _\b")

if opcao == 'a' or opcao == 'A':
	# ----------------------- ### LETRA A ### ----------------------- #
	### 	Calcule a quantidade de diferentes subsequencias de  	###
	### 	tamanho 5 (cinco) que estao presentes na sequencia W 	###
	for i in range(len(conteudoFinal)):	# loop para percorrer o conteudo do arquivo
		if len(str(conteudoFinal[i: i + 5])) >= 5:	# apenas considera os codons de tamanho 5
			codonsList.append(str(conteudoFinal[i: i + 5]))	# adiciona codons a lista
			contaCodons += 1	# incrementa o contador de codons
			i += 1	# incrementa o contador interno

	codonsList = list(set(codonsList))	# elimina elementos repetidos da lista

	print "Letra A"
	print "Lista de todos os possiveis codons:"
	print codonsList
	print "A quantidade de codons diferentes: " + str(len(codonsList))
		# ----------------------- ### LETRA A ### ----------------------- #

if opcao == 'b' or opcao == 'B':
	# ----------------------- ### LETRA B ### ----------------------- #
	subs = conteudoFinal.split('TTT')	# separa as subsequencias limitadas por X
	
	print "Letra B"
	print "Lista das subsequencias separadas por X (TTT):"
	print subs
	print "Quantidade de Subsequencias: " + str(len(subs))
	# ----------------------- ### LETRA B ### ----------------------- #

if opcao == 'c' or opcao == 'C':
	# ----------------------- ### LETRA C ### ----------------------- #
	conteudoA = conteudoFinal 	
	codonsListA = codonsList
	conteudoT = conteudoFinal 	
	codonsListT = codonsList
	conteudoG = conteudoFinal 	
	codonsListG = codonsList
	conteudoC = conteudoFinal 	
	codonsListC = codonsList

	print "Letra C"
	seletor = raw_input("Insira S (A, T, G ou C): ")

	if seletor == 'A' or seletor == 'a':
		contaCodons = 0
		i = 0
		# S = A
		for i in range(len(conteudoA)):	# loop para percorrer o conteudo do arquivo
			if len(str(conteudoA[i: i + 5])) >= 5:	# apenas considera os codons de tamanho 5
				# so permite salvar as subsequencias com S = A
				if conteudoA[i] == 'A' and conteudoA[i+2] == 'A' and conteudoA[i+4] == 'A':
					codonsListA.append(str(conteudoA[i: i + 5]))	# adiciona codons a lista
					contaCodons += 1	# incrementa o contador de codons
					i += 1	# incrementa o contador interno

		codonsListA = list(set(codonsListA))	# elimina elementos repetidos da lista
		print codonsListA
		print "Quantidade de codons com S = A: " + str(len(codonsListA))

	
	if seletor == 'T' or seletor == 't':
		contaCodons = 0
		i = 0
		# S = T
		for i in range(len(conteudoT)):	# loop para percorrer o conteudo do arquivo
			if len(str(conteudoT[i: i + 5])) >= 5:	# apenas considera os codons de tamanho 5
				# so permite salvar as subsequencias com S = A
				if conteudoT[i] == 'T' and conteudoT[i+2] == 'T' and conteudoT[i+4] == 'T':
					codonsListT.append(str(conteudoT[i: i + 5]))	# adiciona codons a lista
					contaCodons += 1	# incrementa o contador de codons
					i += 1	# incrementa o contador interno

		codonsListT = list(set(codonsListT))	# elimina elementos repetidos da lista
		print codonsListT
		print "Quantidade de codons com S = T: " + str(len(codonsListT))

	if seletor == 'G' or seletor == 'g':
		contaCodons = 0
		i = 0
		# S = G
		for i in range(len(conteudoG)):	# loop para percorrer o conteudo do arquivo
			if len(str(conteudoG[i: i + 5])) >= 5:	# apenas considera os codons de tamanho 5
				# so permite salvar as subsequencias com S = A
				if conteudoG[i] == 'G' and conteudoG[i+2] == 'G' and conteudoG[i+4] == 'G':
					codonsListG.append(str(conteudoG[i: i + 5]))	# adiciona codons a lista
					contaCodons += 1	# incrementa o contador de codons
					i += 1	# incrementa o contador interno

		codonsListG = list(set(codonsListG))	# elimina elementos repetidos da lista
		print codonsListG
		print "Quantidade de codons com S = G: " + str(len(codonsListG))

	if seletor == 'C' or seletor == 'c':
		contaCodons = 0
		i = 0
		# S = C
		for i in range(len(conteudoC)):	# loop para percorrer o conteudo do arquivo
			if len(str(conteudoC[i: i + 5])) >= 5:	# apenas considera os codons de tamanho 5
				# so permite salvar as subsequencias com S = A
				if conteudoC[i] == 'C' and conteudoC[i+2] == 'C' and conteudoC[i+4] == 'C':
					codonsListC.append(str(conteudoC[i: i + 5]))	# adiciona codons a lista
					contaCodons += 1	# incrementa o contador de codons
					i += 1	# incrementa o contador interno

		codonsListC = list(set(codonsListC))	# elimina elementos repetidos da lista
		print codonsListC
		print "Quantidade de codons com S = C: " + str(len(codonsListC))
	# ----------------------- ### LETRA C ### ----------------------- #

if opcao == 'd' or opcao == 'D':
	# ----------------------- ### LETRA D ### ----------------------- #
	conteudoInv = conteudoFinal[::-1]	# inverte a string conteudo, para poder ler da direita para a esquerda

	contaCodons = 0
	i = 0

	for i in range(len(conteudoFinal)):	# loop para percorrer o conteudo do arquivo
		if len(str(conteudoFinal[i: i + 7])) >= 7: # apenas considera os codons de tamanho 7
			if conteudoFinal[i] == conteudoFinal[i+6] and conteudoFinal[i+1] == conteudoFinal[i+5] and conteudoFinal[i+2] == conteudoFinal[i+4]:	
				codonsList.append(str(conteudoFinal[i: i + 7]))	# adiciona codons a lista
				contaCodons += 1	# incrementa o contador de codons
				i += 1	# incrementa o contador interno

	codonsList = list(set(codonsList))	# elimina elementos repetidos da lista

	contaCodons = 0
	i = 0

	for i in range(len(conteudoInv)):	# loop para percorrer o conteudo do arquivo
		if len(str(conteudoInv[i: i + 7])) >= 7: # apenas considera os codons de tamanho 5
			if conteudoInv[i] == conteudoInv[i+6] and conteudoInv[i+1] == conteudoInv[i+5] and conteudoInv[i+2] == conteudoInv[i+4]:	
				codonsList.append(str(conteudoInv[i: i + 7]))	# adiciona codons a lista
				contaCodons += 1	# incrementa o contador de codons
				i += 1	# incrementa o contador interno

	codonsList = list(set(codonsList))	# elimina elementos repetidos da lista

	print "Letra D"
	print "Lista de todos os possiveis codons"
	print codonsList
	print "A quantidade de codons diferentes: " + str(len(codonsList))
	# ----------------------- ### LETRA D ### ----------------------- #

if opcao == 'e' or opcao == 'E':
	# ----------------------- ### LETRA E ### ----------------------- #
	i = 0

	# faz a alteracao do DNA para as bases corretas
	for i in range(len(conteudoFinal)):
		conteudoFinal = conteudoFinal.replace("A","U")
		conteudoFinal = conteudoFinal.replace("T","D")
		conteudoFinal = conteudoFinal.replace("C","B")
		conteudoFinal = conteudoFinal.replace("G","E")
		i += 1

	i = 0

	for i in range(len(conteudoFinal)):
		conteudoFinal = conteudoFinal.replace("E","C")
		conteudoFinal = conteudoFinal.replace("B","G")
		conteudoFinal = conteudoFinal.replace("D","A")
		i += 1

	print conteudoFinal

	i = 0

	for i in range(len(conteudoFinal)):	# loop para percorrer o conteudo do arquivo
		if len(str(conteudoFinal[i: i + 3])) >= 3:	# apenas considera os codons de tamanho 5
			codonsList.append(str(conteudoFinal[i: i + 3]))	# adiciona codons a lista
			contaCodons += 1	# incrementa o contador de codons
			i += 1	# incrementa o contador interno

	print "Letra E"
	print "Os 3 principais frames obtidos foram:"
	frames = collections.Counter(codonsList)
	print frames.most_common(3)
	# ----------------------- ### LETRA E ### ----------------------- #
	