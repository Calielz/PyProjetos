NumInt = []
valor = int(input("digite um número: "))

while valor != 0:
  NumInt.append(valor)
  valor = int(input("digite um número: "))
    


print(f' Lista: {NumInt}, contém {len(NumInt)} elementos. ')