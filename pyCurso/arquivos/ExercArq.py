produto = {}
for linhas in open("arquivos/ExercArq.txt"):
  lst = linhas.rstrip().split(';')
  cod = int(lst[0])
  qtde = int(lst[1])
  if cod in produto:
    produto[cod] += qtde
  else:
    produto[cod] = qtde

for cod in produto.items():
 print(f'Código do produto: {cod[0]}  Quantidade: {cod[1]} ')
  
