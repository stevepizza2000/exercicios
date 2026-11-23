
#recebo a lista de numeros(pode ser vazia)
#pego o tamanho da lista
#checo numero por numero e os somo
#caso não exista numeros dentro da lista retorna zero
#faco a media com a soma dos numeros e o tamanho da lista
#checo quais numeros são maiores do que a media
#guardo esses numeros
#printo apenas a quantidade de numeros maiores


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