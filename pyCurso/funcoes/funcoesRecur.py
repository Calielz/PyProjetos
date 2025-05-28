def Fatorial(N):
    if N <= 1:
      return 1
    else:
      print(N)
      return N * Fatorial(N-1) # esse retorno só é retornado até que a função seja respondida
    ''' return 4 * fatorial(4-1=3) ele não retorna ainda pq a função chamada, não foi resolvida
        return 3 * fatorial(3-1=2)
        return 2 * fatorial(2-1=1)  agora lá em cima é retornado 1 pra resposta do fatorial dessa linha aqui, então é como se essa chamada da função virasse um 1
        assim eu obtenho a resposta pra função do return 3 que agora é 2 "return 3 * 2" assim por diante
                                                                          "return 4* 6"= 24 retornando no programa principal
        ele vai respondendo as funções do segundo retorno, até que o primeiro retorno seja respondido, assim, ele vai resolver os returns do passado pra só assim retornar algo pro programa principal.
    
    '''
Entrada = int(input('Digite um inteiro: '))
F = Fatorial(Entrada)
print(f'O fatorial de {Entrada} é {F}')