n = -1
while n != 0:
  n = int(input('digite um inteiro: '))
  match n:
    case 1: 
      print("você digitou um")
    case 2: 
      print("você digitou dois")
    case 3: 
      print("você digitou três")
    case _: #case _ tem que ser o ultimo
          print("você digitou outra coisa")

  

