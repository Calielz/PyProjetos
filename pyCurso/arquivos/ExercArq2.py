from random import randint
arq = open("arquivos/numeros.txt", "w")
qtd = int(input("digite a quantidade: "))
for x in range(qtd):
  arq.write(f' {randint(1, 5000)}\n')

arq.close()