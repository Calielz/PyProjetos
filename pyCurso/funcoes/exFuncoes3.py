def parImpar(numInt):
  if numInt % 2 ==0:
    return 'Par'
  else:
    return 'Impar'
  #if inline:return 'Par' if numInt % 2 ==0 else 'Impar'

x = int(input('Digite um inteiro: '))
print(parImpar(x))
