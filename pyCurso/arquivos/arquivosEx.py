disciplinas = ("Matemática", "Português", "História", "Geografia", "Física", "Química", "Biologia")
notas = [8.7, 10, 9, 6.8, 5.5, 10, 8]
arq = open("arquivos/arquivosEx.txt", "w")

for i in range(len(notas)):
  arq.write(f'A nota de {disciplinas[i]} foi: {notas[i]}\n ')
  
arq.close()