LL = int(input("digite a linha de calçados"))
match LL:
  case 16:
    print("bebê")
  case 49:
    print("masculino esportivo")
  case 23:
    print("infantil feminino")
  case 52:
    print("Feminino formal salto baixo")
  case 25:
    print("Infantil masculino")
  case 53:
    print("Feminino formal salto alto")
  case 29:
    print("Infantil esportivo")
  case 56:
    print("Feminino casual salto alto")
  case _:
    print("Código inválido")