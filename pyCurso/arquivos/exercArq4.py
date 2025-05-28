Veiculo = {}
while True:
  placa = input("Insira a placa do veículo, em letras maiúsculas: ")
  if placa.upper() == 'FIM':
    print("Programa encerrado.")
    break
  elif placa in Veiculo:
    confirm = (input('essa placa já existe, deseja alterar? s/n '))
    if confirm == 's':
      Veiculo.update({placa: (marca, modelo, tipo, kms, dataComp) })
    elif confirm == 'n':
      print("contato mantido.")
      continue
    else:
      print("Entrada inválida.")
      continue

  
  marca = input("Insira a marca do veículo: ")
  modelo = input("Insira o modelo do veículo: ")
  tipo = input("Insira o tipo do veículo(caminhão, carro, motocicleta, etc.): ")
  kms = int(input("Insira a kilometragem do veículo: "))
  dataComp = input("Insira a data de compra do veículo(AAAA/MM/DD): ")

  Veiculo[placa.upper()] = (marca, modelo, tipo, kms, dataComp)

arq = open("arquivos/frotaVeiculos.txt", "w")
for placa, dados in Veiculo.items():
  arq.write(f'{placa};{dados[0]};{dados[1]};{dados[2]};{dados[3]};{dados[4]}\n')
arq.close()
  
  
