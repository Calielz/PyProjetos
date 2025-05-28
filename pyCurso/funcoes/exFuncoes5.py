def CalcDigito(cod):
  s = str(cod)
  p = 2
  som = 0
  for a in s:
    som += p * int(a)
    p +=1
  return som % 7

codigo = int(input("digite o Código do produto(de 10000 a 99999): "))
if codigo >= 10000 and codigo <= 99999:
    digito = CalcDigito(codigo)
    print(f'Código: {codigo} -> dígito: {digito}')
    codigo = int(input('Digite o código: '))
else:
    print("informe apenas códigos de 10000 a 99999. ")
print("fim do Programa.")