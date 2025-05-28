negativo = []
positivo = []

for i in range(10):
  num = int(input("digite um número inteiro: "))
  if num >= 0:
    positivo.append(num)
  else:
    negativo.append(num)

print(negativo)
print(positivo)
