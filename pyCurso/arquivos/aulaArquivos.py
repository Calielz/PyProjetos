#open("caminho","r") # abertura do arquivo e o modo que usaremos, sempre lembrar de fechar!

# Mode
# r - Leitura
# a - Append / incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

#diferença do a pro w = o a incrementa no arquivo que já existe, e w  limpa o arquivo se já existir e incrementa, além de criar um novo arquivo 
# arquivo = open("arquivos/testArquivo3.txt", "r") # é possível criar arquivos com modos de gravação/escrita a, w, x

# print(arquivo.readable()) #verifica se o arquivo é possível ler
# print(arquivo.read()) #lê o arquivo, só possível em modo de leitura
# print(arquivo.readline()) #lê a primeira linha do arquivo  e avança para a próxima linha
# print(arquivo.readline())

# lista = print(arquivo.readlines()) #retorna uma lista de strings 
# print(lista)
# print(lista[0])

# arquivo.write("Javascript\n") #escreve no arquivo, incrementação




# arquivo.close() #sempre fechar o arquivo

#Pastas
# import os

# os.remove("arquivos/testArquivo4.txt") # remover um arquivo, se ele não estiver fechado, dá erro, usar com w

# os.rmdir("arquivos/novapasta") # remover uma pasta, só é possivel se estiver vazia
