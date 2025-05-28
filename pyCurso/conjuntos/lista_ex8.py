from random import randint
lst = []
qtde = int(input("digite a quantidade: "))
for i in range(qtde):
  lst.append(randint(1, 20))
print(lst)
x = 1
while x > 0:
  x = int(input("digite X:"))
  if x in lst:
    print(f' esse número aparece {lst.count(x)} vezes na lista.')
  else: 
    print("esse número não está na lista")
