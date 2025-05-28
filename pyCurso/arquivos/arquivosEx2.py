arq = open("arquivos/numerosInteiros.txt", "w")
numInt = int(input("Digite um número inteiro: "))
while numInt != 0:
  arq.write(f' {numInt}\n')
  numInt = int(input("Digite um número inteiro: "))
arq.close()