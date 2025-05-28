lst = []
for linha in open("arquivos/numeros.txt"):
  lst.append(int(linha.rstrip()))

lst.sort()

arq = open("arquivos/ordenados.txt", "w")
for i in range(len(lst)):
  arq.write(f'{lst[i]}\n')
arq.close()
