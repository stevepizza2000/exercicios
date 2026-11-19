def media_acima(numeros):
    soma = 0
    tamanho = len(numeros)
    media = None
    
    for numero in numeros:
        if numero == None:
            return 0
        soma += numero
        

    media = soma / tamanho

    for i in numeros:
        if i > media:

    
    
        
    

    
print(media_acima([1, 2, 3, 4, 5]))   # 2  (média 3; acima: 4 e 5)
print(media_acima([10, 10, 10]))      # 0
print(media_acima([-5, 5]))           # 1
print(media_acima([1, 1, 1, 9]))      # 1  (média 3)
print(media_acima([7]))               # 0
print(media_acima([]))                # 0