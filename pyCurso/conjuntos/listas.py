lista = [35,34,54,22,13, 17, 21] # listas são ordenadas e mutáveis, duplicadas OK, pode tudo aqui
print(lista)
i = 0
while i < len(lista):
    print(lista[i], end='  ') #exibição dos elementos
    i = i + 1
print("fim")

print(lista[0])
print(lista[2])

lista.append(37) #adicionar elementos
print(lista)

lista.remove(17) #remover
print(lista)
lista.pop(0)
print(lista)
del lista[0]
print(lista)

'''fatiamento'''
print(lista[3:6]) #(inicial:final: pulo)
print(lista[1:6:2])

b = lista[:] #copia da lista ou b= lista.copy()
b[0] = 99
print(b)
print(lista)

'''métodos de listas:
clear: limpa toda a lista
copy: retorna uma cópia da lista
count: conta quantos elementos de um determinado valor existem na lista
extend: adicionar uma lista a outra
index:retorna a posição de um elemento
insert:inclusão de um elemento em qualquer posição da lista, diferente do append
pop: remove um elemento da lista pelo índice, diferente de remove, que remove o elemento em si
reverse: inverte a lista
sort: ordena a lista em ordem crescente, se usar reverse= true, descrescente
'''
