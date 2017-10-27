import os

os.system("cls")

print '\n\t\tDESAFIO COMPUTACIONAL II'
print '\t\t\tMENU'
print '\n1 - Alinhamento de Sequencias (Matrizes de Ponto)'
print '2 - Alinhamento de Sequencias (Needleman-Wunsch)'
opcao = input('\nEscolha: _\b')

if opcao == 1:

	# fileName = raw_input("Insira o nome do arquivo que contem as sequencias: _\b")
	varFile = open("seq1.txt","r")	# abre o arquivo em modo leitura

	print("Serao gerados dois arquivos .txt com as matrizes de pontos dos alinamentos")
	print("(Homo sapiens x Mus musculus) e (Homo sapiens x Rattus norvegicus).")

	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	homo = varFile.readline() + varFile.readline() + varFile.readline() + varFile.readline()
	homo = homo.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	mus = varFile.readline() + varFile.readline() + varFile.readline() + varFile.readline()
	mus = mus.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	rattus = varFile.readline() + varFile.readline() + varFile.readline()
	rattus = rattus.replace("\n","")
		
	matrizFinal1 = []
	matrizImpressa1 = []
	matrizFinal2 = []
	matrizImpressa2 = []
	resultadoFinal1 = 0
	resultadoFinal2 = 0
	resultadoIdentidade1 = 0
	resultadoIdentidade2 = 0
	tamHomo = len(homo)
	tamMus = len(mus)
	tamRat = len(rattus)

	for i in range(tamHomo):
		linha = []
		for j in range(tamMus):
			if homo[i] == mus[j]:
				linha = linha + [1]
			if homo[i] != mus[j]:
				linha = linha + [0]
		matrizFinal1 = matrizFinal1 + [linha]

	for i in range(tamHomo):
		for j in range(tamMus):
			if i == j and matrizFinal1[i][j] == 1:
				resultadoFinal1 += 1

	for i in range(tamHomo):
		for j in range(tamMus):
			if matrizFinal1[i][j] == 1:
				resultadoIdentidade1 += 1

	for i in range(tamHomo):
		linha = []
		for j in range(tamMus):
			if homo[i] == mus[j]:
				linha = linha + [1]
			if homo[i] != mus[j]:
				linha = linha + [0]
		matrizImpressa1.append('N')
		matrizImpressa1 = matrizImpressa1 + [linha]

	# print matrizFinal1
	matrizImpressa1 = str(matrizImpressa1).replace("N","\n")

	varFile = open("matriz1.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizImpressa1))
	varFile.close()
	print "\n\nGerado o arquivo 'matriz1.txt' (Homo sapiens x Mus musculus)"

	for i in range(tamHomo):
		linha = []
		for j in range(tamRat):
			if homo[i] == rattus[j]:
				linha = linha + [1]
			if homo[i] != rattus[j]:
				linha = linha + [0]
		matrizFinal2 = matrizFinal2 + [linha]

	for i in range(tamHomo):
		for j in range(tamRat):
			if i == j and matrizFinal2[i][j] == 1:
				resultadoFinal2 += 1

	for i in range(tamHomo):
		for j in range(tamRat):
			if matrizFinal2[i][j] == 1:
				resultadoIdentidade2 += 1

	for i in range(tamHomo):
		linha = []
		for j in range(tamRat):
			if homo[i] == rattus[j]:
				linha = linha + [1]
			if homo[i] != rattus[j]:
				linha = linha + [0]
		matrizImpressa2.append('N')
		matrizImpressa2 = matrizImpressa2 + [linha]

	# print matrizFinal2
	matrizImpressa2 = str(matrizImpressa2).replace("N","\n")

	varFile = open("matriz2.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizImpressa2))
	varFile.close()
	print "Gerado o arquivo 'matriz2.txt' (Homo sapiens x Rattus norvegicus)"
	wait = raw_input("Pressione qualquer tecla para continuar...")
	print "\n"

	identidade1 = (resultadoFinal1 * 2)/(tamHomo + tamMus)
	identidade2 = (resultadoFinal2 * 2)/(tamHomo + tamRat)

	print "Resultado 1 (Homo sapiens x Mus musculus): \t " + str(resultadoFinal1)
	print "Identidade 1 (Homo sapiens x Mus musculus): \t " + str((resultadoIdentidade1 * 2)/(tamHomo + tamMus)) + "%"
	print "Resultado 2 (Homo sapiens x Rattus norvegicus):  " + str(resultadoFinal2)
	print "Identidade 2 (Homo sapiens x Rattus norvegicus): " + str((resultadoIdentidade2 * 2)/(tamHomo + tamRat)) + "%"
	if identidade1 > identidade2:
		print "A especie que apresenta maior identidade com a Homo sapiens: Mus musculus"
	if identidade1 < identidade2:
		print "A especie que apresenta maior identidade com a Homo sapiens: Rattus norvegicus"

if opcao == 2:

	# fileName = raw_input("Insira o nome do arquivo que contem as sequencias: _\b")
	varFile = open("seq2.txt","r")	# abre o arquivo em modo leitura

	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	rattus = varFile.readline() + varFile.readline() + varFile.readline()
	rattus = rattus.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	homo = varFile.readline() + varFile.readline() + varFile.readline()
	homo = homo.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	lemur = varFile.readline() + varFile.readline() + varFile.readline()
	lemur = lemur.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	mus = varFile.readline() + varFile.readline() + varFile.readline()
	mus = mus.replace("\n","")
	dadoIgnore = varFile.readline() # ignora o conteudo da primeira linha
	whale = varFile.readline() + varFile.readline() + varFile.readline()
	whale = whale.replace("\n","")

	tamHomo = len(homo)
	tamMus = len(mus)
	tamRat = len(rattus)
	tamLem = len(lemur)
	tamWha = len(whale)

	matrizFinal1 = [0]*(tamRat)
	for i in range(tamRat):
		matrizFinal1[i] = [0]*(tamHomo)

	matrizFinal2 = [0]*(tamLem)
	for i in range(tamLem):
		matrizFinal2[i] = [0]*(tamHomo)

	matrizFinal3 = [0]*(tamMus)
	for i in range(tamMus):
		matrizFinal3[i] = [0]*(tamHomo)

	matrizFinal4 = [0]*(tamWha)
	for i in range(tamWha):
		matrizFinal4[i] = [0]*(tamHomo)

	for i in range(tamHomo):
	    for j in range (tamRat):
	        if homo[i] == rattus[j]:
	            Sij = [matrizFinal1[i-1][j-1] + 5, matrizFinal1[i][j-1] - 4, matrizFinal1[i-1][j] -4]
	            matrizFinal1[i][j] = max(Sij)
	        if homo[i] != rattus[j]:
	            Sij = [matrizFinal1[i-1][j-1] -3, matrizFinal1[i][j-1] - 4, matrizFinal1[i-1][j] -4]
	            matrizFinal1[i][j] = max(Sij)

	varFile = open("matriz3.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizFinal1))
	varFile.close()
	print "Gerado o arquivo 'matriz3.txt' (Homo sapiens x Rattus norvegicus)"

	for i in range(tamLem):
	    for j in range (tamHomo):
	        if lemur[i] == homo[j]:
	            Sij = [matrizFinal2[i-1][j-1] + 5, matrizFinal2[i][j-1] - 4, matrizFinal2[i-1][j] -4]
	            matrizFinal2[i][j] = max(Sij)
	        if lemur[i] != homo[j]:
	            Sij = [matrizFinal2[i-1][j-1] -3, matrizFinal2[i][j-1] - 4, matrizFinal2[i-1][j] -4]
	            matrizFinal2[i][j] = max(Sij)

	varFile = open("matriz4.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizFinal2))
	varFile.close()
	print "Gerado o arquivo 'matriz4.txt' (Homo sapiens x Lemur)"

	for i in range(tamHomo):
	    for j in range (tamMus):
	        if homo[i] == mus[j]:
	            Sij = [matrizFinal3[i-1][j-1] + 5, matrizFinal3[i][j-1] - 4, matrizFinal3[i-1][j] -4]
	            matrizFinal3[i][j] = max(Sij)
	        if homo[i] != mus[j]:
	            Sij = [matrizFinal3[i-1][j-1] -3, matrizFinal3[i][j-1] - 4, matrizFinal3[i-1][j] -4]
	            matrizFinal3[i][j] = max(Sij)

	varFile = open("matriz5.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizFinal3))
	varFile.close()
	print "Gerado o arquivo 'matriz5.txt' (Homo sapiens x Mus musculus)"

	for i in range(tamHomo):
	    for j in range (tamWha):
	        if homo[i] == whale[j]:
	            Sij = [matrizFinal4[i-1][j-1] + 5, matrizFinal4[i][j-1] - 4, matrizFinal4[i-1][j] -4]
	            matrizFinal4[i][j] = max(Sij)
	        if homo[i] != whale[j]:
	            Sij = [matrizFinal4[i-1][j-1] -3, matrizFinal4[i][j-1] - 4, matrizFinal4[i-1][j] -4]
	            matrizFinal4[i][j] = max(Sij)

	varFile = open("matriz6.txt","w")	# abre o arquivo em modo escrita
	matrizTxt = varFile.write(str(matrizFinal4))
	varFile.close()
	print "Gerado o arquivo 'matriz6.txt' (Homo sapiens x Whale)"
	wait = raw_input("Pressione qualquer tecla para continuar...")
	print "\n"