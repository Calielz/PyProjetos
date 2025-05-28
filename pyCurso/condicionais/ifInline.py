# #if inline
# x= 10
# y= 11

# print(f'X é maior = {x}') if x >= y else print(f'y é maior = {y}')
# # <comando para verdadeiro> if <condição> else <comando para falso>

#  # o inline-if acima é o mesmo que:
# if x >= y:
#   print(f'X é maior = {x}')
# else:
#   print(f'Y é maior = {y}')

Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216] 
Lista = []
print('Alternativa com if clássico')
for codigo in Codigos:
 if codigo >= 120 and codigo <= 200:
  Lista.append(codigo)
print(f' códigos filtrados -> {Lista}')

print('\nAlternativa com if de única linha')
Lista = []
for codigo in Codigos:
 Lista.append(codigo) if codigo >= 120 and codigo <= 200 else 0 #necessita do else
print(f' códigos filtrados -> {Lista}')

#retorno de valor
X = int(input('Digite um inteiro: '))
paridade = 'par' if X % 2 == 0 else 'ímpar'
print(f'O valor {X} é {paridade}')
