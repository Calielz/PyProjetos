produtos = {}
while True:
  cod = input("Digite o código do produto: ")
  if cod == '':
    break
  elif cod in produtos:
    print("este produto já existe.")
    continue
  preco = float(input("informe o preço do produto: "))
  produtos[cod] = preco

for cod in produtos:
  print(f'Código do produto: {cod} - Preço: {produtos[cod]}')
