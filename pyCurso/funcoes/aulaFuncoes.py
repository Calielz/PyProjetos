#uma função é um bloco de código ao qual se atribui um nome identificador e que executa certa tarefa, podendo receber parâmetros de entrada bem como produzir e retornar algum resultado. ajuda na reutilização de códigos, manutenção, ajuda a dividir um problema em partes menores

#a função pode ou não retornar dados, de qualquer tipo e de qualquer quantidade, como mostrado abaixo. 
def GeraDados():
 """Esta função inicializa 7 objetos de diferentes classes e os retorna"""
 a = 16
 b = 39.7
 c = 'texto'
 d = [1, 2, 3, 4]
 e = (0, 1)
 f = {80, 90, 100}
 g = frozenset((3, 4, 5))
 return a, b, c, d, e, f, g
 # Este retorno equivale a uma tupla. É o mesmo que (a, b, c, d, e, f, g)
Dados = GeraDados()
print('Relação de elementos gerados na função')
for x in Dados:
 print(f' {x} é objeto da classe {type(x)}')

 #com os parâmetros, fornecemos dados de entrada que possam ser usados no seu código interno.
from random import randint
def CarregaLista(qtde, a, b):
    L = []
    for i in range(qtde):
      L.append(randint(a, b))
      return L
    
q = int(input('Digite a quantidade desejada: '))
lmin = int(input('Digite o limite mínimo: '))
lmax = int(input('Digite o limite máximo: '))
valores = CarregaLista(q, lmin, lmax)
print(f'Lista gerada >> {valores}')
print(f'A lista gerada tem {len(valores)} elementos')
