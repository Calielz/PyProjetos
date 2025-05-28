'''como sabemos objetos fora de função são globais, e dentro são locais, que só vão existir quando a função é chamada'''
#cuidado com os nomes de objetos 
def funcao1():
  print('dentro da função1 temos >>', a, b)
def funcao2():
  a = 100
  b = 200
  print('dentro da função2 temos >>', a, b)
  
a = 10
b = 20
funcao1() #dentro da funcao1() não há declaração de qualquer objeto, então a função usou os objetos a e b globais
funcao2() #objetos locais a e b foram criados e carregados com 100 e 200. Nessa saída foram usados os objetos locais, uma vez que eles existem na funcao2()
print('fora da função temos >>', a, b) # agora foram usados os objetos globais, na parte principal do programa

'''global'''
def funcao1():
    print('dentro da função1 temos >>', a, b)
def funcao2():
    global a # nesta linha informamos que a é o objeto global
    a = 100 # nesta linha estamos alterando o valor do a global, vai refletir fora da função também
    b = 200 # nesta linha estamos criando um objeto local b
    print('dentro da função2 temos >>', a, b)
#Objeto global é manipulável dentro da função apenas se for qualificado com a palavra global

a = 10
b = 20
funcao1()
funcao2()
print('fora da função temos >>', a, b) #O valor original 10 de a foi alterado dentro da função para 100.
#por isso evite usar nomes idênticos para objetos locais e globais