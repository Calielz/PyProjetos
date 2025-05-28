Contatos = {}
while True:
  nome = input("insira o nome: ")
  if nome == '':
    print("programa encerrado.")
    break
  elif nome in Contatos:
    confirm = (input('esse contato já existe, deseja alterar? s/n '))
    if confirm == 's':
      Contatos.update({nome: dicItem}) #jeito de dicionário
      #Contatos.update({nome: (numCel, email, datNiver) }) #jeito de tupla
    
    elif confirm == 'n':
      print("contato mantido.")
      continue
    else:
      print("Entrada inválida.")
      continue
  numCel = input("digite o número do celular: ")
  email = input("informe o Email: ")
  datNiver = input("informe a data de aniversário: ")

  dicItem = {'celular': numCel, 'email': email, 'aniversario': datNiver }# jeito de dicionário
  #Contatos[nome] = (numCel, email, datNiver) # Jeito de tupla
  Contatos[nome] = dicItem #jeito de dicionário
  
print("FIM.")

for nome, dados in Contatos.items():
  print(nome, dados['celular'], dados['email'], dados['aniversario']) # jeito de dicionário
  #print(nome, dados[0], dados[1], dados[2]) # jeito de tupla
