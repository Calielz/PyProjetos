lista = []
Num = float(input("Digite um número Real, 0 para encerrar."))
while Num != 0:
  lista.append(f'{Num:.3f}\n')
  Num = float(input("Digite um número Real:"))

print(lista)
# arq = open("arquivos/numerosReais.txt", "w")
# arq.writelines(lista)
# arq.close()