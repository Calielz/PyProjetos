qtd = int(input("digite a quantidade de números"))
num = []
for i in range(qtd):
  x= float(input(f' elemento{i}: '))
  num.append(x)

for valor in num:
  print(f' {valor}')
