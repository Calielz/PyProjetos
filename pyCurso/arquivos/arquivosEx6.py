estoque = {}
for linhas in open("arquivos/arquivosEx6.txt"):
  lst = linhas.rstrip().split(';') #strip remove \n, split separa de acordo com o ;
  cod = int(lst[0])
  qtde = int(lst[1])
  precoUnit = float(lst[2])
  estoque[cod] = (qtde, precoUnit)
print("valores carregados no dicionário")
print(estoque)
print('\nExibição dos dados na forma de tabela')
TotGeral = 0
for cod, dados in estoque.items():
 tot = dados[0] * dados[1]
 TotGeral += tot
 print(f' {cod}: {dados[0]:5d} x {dados[1]:6.2f} = {tot:8.2f}')
print(' ' * 24, f'{TotGeral:8.2f}')
print('\nFim do Programa')