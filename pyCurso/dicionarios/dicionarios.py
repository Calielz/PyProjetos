#dicionários são coleções com chave-valor, basicamente uma tupla com chave da minha escolha
UF = {'SE' : 'Sergipe', 'BA': 'Bahia', 'CE' : 'Ceará'} 
print(UF)

'''UF = {}  #como adicionar dados num dic vazio
UF['SP'] = 'São Paulo'
print(UF)'''

# se a chave não existe no dicionário, então o elemento é criado; se a chave já existe no dicionário, então o elemento é alterado;
D = {}
D['a'] = 120
print(D)
D['a'] = 240
print(D)
D['b'] = 100
x = D['a'] + D['b']
print(x)
# tudo que é imutável pode ser colocado em um dicionário.

#fromkeys: funão que permite criar um dicionário com as chaves previstas e um valor padrão que pode ser mudado depois
codigos = (111, 139, 143, 157)
A = {}
A = {}.fromkeys(codigos, '')
print(A)

for x in UF.keys(): #iteração com a chave do dict
  print(f' {x} - {UF[x]}')

'''for x in UF.values(): #iteração com o valor do dict
  print(f'  {x}')

for x in UF.items(): #iteração com os itens do dict, imprime as tuplas
  print(f'{x[0]} - {x[1]}') #o primeiro X é a chave, o segundo é o valor

for chave, valor in UF.items(): #outra forma
  print(f'{chave} - {valor}')'''
