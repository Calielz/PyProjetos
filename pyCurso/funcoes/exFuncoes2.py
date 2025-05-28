def Saudacao(nome, mensagem = 'olá'): # a mensagem vira um parâmetro opicional com valor padrão, se não for fornecido um valor, o "olá" é usado, enquanto "nome" é um parâmetro obrigatório.
  print(mensagem, nome)
Saudacao('josé')
Saudacao('josé', 'bla bla bla')

'''parâmetros posicionados'''
def diferenca (a, b):
  return a-b
x = 12
y = 7
print(diferenca(x, y)) # x recebe a e y recebe b, parâmetro posicionado
print(diferenca(b=x, a=y)) #agora definimos que x recebe b e y recebe a, parâmetro nomeado
#ordem sempre será parâmetros posicionados e depois os nomeados, não pode haver posicionados depois de nomeados.

'''empacotamento de parâmetros'''
def Somatoria(*dados): #não sabendo o número de parâmetros podemos usar essa estrutura "*"
    r = 0
    for i in dados:
      r += i
    return r
a = Somatoria(3,5,1)
print(a)
print(Somatoria(10,10))

def MontaSaida(*valores, separador = ', '):
  saida = separador.join(valores)
  return saida
print(MontaSaida('olá', 'sou', 'caliel'))
print(MontaSaida('olá', 'sou', 'caliel', separador='...')) # após o parâmetro empacotado, o parâmetro tem que ser nomeado, no caso o separador
#parâmetros normais sempre vão estar antes de parâmetros empacotados, ordem: parâmetros normais -> parâmetros empacotados -> parâmetros nomeados

'''Desempacotamento de parâmetros'''
def Calcula(a, b, c): # recebe 3 parâmetros normais
   return (a + b) / c

L1 = [12, 20, 5] # agora temos o contrário do empacotamento, os valores já estão em uma lista e vão ser distribuidos nos parâmetros.
print(Calcula(*L1)) #caso não usasse o desempacotamento, parâmetro 'a' iria receber L1 todo.
L2 = [1,2,3,4]
# print(Calcula(*L2))# a quantidade de elementos tem que coincidir com a quantidade de parâmetros.
#a chamada da função deve conter um objeto de classe sequência, string, tupla ou lista

