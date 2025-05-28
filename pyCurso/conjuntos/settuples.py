frutas = {"banana", "maçã", "abacaxi", "laranja", "coco"} #"set" são desordenados e imutáveis, mas podemos adicionar e remover, não são aceitas duplicatas como em listas.
print(dir(frutas))

carros = ("fastback", "jetta", "nivus", "cronos") #tuplas são ordenadas e não podem ser mudadas, sem remove, add e mudanças, duplicatas OK, são mais rápidas
print(dir(carros))

texto = 'qualquer texto'
c1 = set(texto)
print(c1)

conjunto = { 45.4, 1.6, 65.2, 15.6 }
for c in conjunto:
  print(c)

print("sksks")
conjunto = {45.4, 15.6,65.2, 1.6}
for c in conjunto:
  print(c)

'''from random import randint #exemplo de iteração em sets, como não há duplicatas de valores, é rodado até achar um valor único
qtde = int(input('digite a quantidade de elementos: '))
while qtde > 50:
  print("valor muito alto")
  qtde = int(input('Digite a quantidade de elementos (max 50): '))

conjunto = set()
while len(conjunto) < qtde:
  conjunto.add(randint(1, 50 ))
print(conjunto)
print(f'o conjunto tem {len(conjunto)} elementos') '''