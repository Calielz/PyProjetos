NumInt = []
valor = int(input("digite um número: "))

while valor != 0:
   if valor not in NumInt :
    NumInt.append(valor)
    
   else:
     print("esse valor já está na lista")
     
   valor = int(input("digite um número: "))


print(f' Lista: {NumInt}, contém {len(NumInt)} elementos. ')