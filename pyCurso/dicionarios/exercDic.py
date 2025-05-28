produtos = {}
cod = input("forneça o código do produto, para terminar,digite vazio: ")
while cod != '':
  preco = float(input("forneça o preço: "))
  produtos [cod] = preco
  cod = input("forneça o código do produto:")

for cod in produtos.keys():
  print(f'{cod} - {produtos[cod]}')
  