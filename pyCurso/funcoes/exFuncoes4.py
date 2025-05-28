def Divisiveis(a, b):
  print(a/ b)
  return True if a % b == 0 else False

num1 = int(input("informe o primeiro número: "))
num2 = int(input("informe o segundo número: "))

if (Divisiveis(num1, num2)):
  print(f'{num1} é divisível por {num2}')
else:
  print(f'{num1} não é divisível por {num2}')

