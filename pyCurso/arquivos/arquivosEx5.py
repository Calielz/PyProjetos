lst = []
for linha in open("arquivos/arquivosEx4.txt"): #exercício para substituir o readline e o laço while
  lst.append(int(linha))

print(lst)
Soma = sum(lst)
print(f'soma dos valores: {Soma}')
qtde = len(lst)
print(f'Quantidade de valores: {qtde}')
print(f'média dos valores: {Soma/ qtde}')
minimo = min(lst)
print(f'Mínimo: {minimo}')
Máximo = max(lst)
print(f'Máximo: {Máximo}')
