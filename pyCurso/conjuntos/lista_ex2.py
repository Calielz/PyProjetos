P = int(input("digite o primeiro termo: "))
R = int(input("digite a razão: "))
Q = int(input("digite a quantidade: "))
Termos = [P]
a = 0
while a < Q-1:
  P = P + R
  Termos.append(P)
  a += 1
print(Termos)
