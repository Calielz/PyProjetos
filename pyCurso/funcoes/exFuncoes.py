def operacoes(a, b):
  soma = a+b
  subt = a-b
  div = a/b
  mult = a*b
  return soma, subt, div, mult 

v1 = float(input("Informe o primeiro valor: "))
v2 = float(input("Informe o segundo valor: "))

resultados = operacoes(v1, v2)
print(f' soma = {resultados[0]:.2f}')
print(f' diferença = {resultados[1]:.2f}')
print(f' multiplicação = {resultados[2]:.2f}')
print(f' divisão = {resultados[3]:.2f}')
