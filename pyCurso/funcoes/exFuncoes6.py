def matT (lista):
    # result = (sum(lista), sum(lista)/len(lista), min(lista), max(lista) )

    #soma
    soma = 0
    for n in lista:
        soma += n

    #media
    qtd = 0
    for n in lista:
        qtd += 1
    media = soma / qtd 

    #mínimo
    min = lista[0]
    for n in lista:
        if n < min:
            min = n

    #máximo
    max = lista[0]
    for n in lista:
        if n > max:
            max = n

    result = (soma, media, min, max)

    
    return result

lista1 = [2, 4, 6, 2]
print(matT(lista1))
