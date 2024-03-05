# open é uma funçao q permite abrir um arquivo, ler ou escrever neste arquivo
arq = open("dados.txt","a")
#a função write permite escreve em um arquivo
arq.write("Olá \n")
# fecha o arquivo retirando-o da memória
arq.close()