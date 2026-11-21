def media_acima(numeros):
    soma = 0
    tamanho = len(numeros)
    contador = 0

    if tamanho == 0:
        return 0
    
    for numero in numeros:
        soma += numero
        

    media = soma / tamanho

    for i in numeros:
        if i > media:
            contador += 1
        
    return contador
    
print(media_acima([1, 2, 3, 4, 5]))   # 2  (média 3; acima: 4 e 5)
print(media_acima([10, 10, 10]))      # 0
print(media_acima([-5, 5]))           # 1
print(media_acima([1, 1, 1, 9]))      # 1  (média 3)
print(media_acima([7]))               # 0
print(media_acima([]))                # 0