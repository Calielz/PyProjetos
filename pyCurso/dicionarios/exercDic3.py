UF = {}
while True:
  sigla = input("Digite a sigla do Estado: ")
  if sigla == '':
    print("Programa encerrado.")
    break
  elif sigla in UF:
    print("esse Estado já está cadastrado.")
    continue
  nome = input("Digite o nome do Estado: ")
  capital = input("Digite o nome da Capital: ")
  PIB = float(input("Informe o PIB do Estado: "))

  UF[sigla] = (nome, capital, PIB)

print(' {:15} {:15} {:>10}'.format('Estado', 'Capital', 'PIB (R$ bi)'))
for sigla, dados in UF.items():
 print('({}) {:15} {:15} {:10.1f}'.format(
 sigla,
 dados[0],
 dados[1],
 dados[2] )
 )
