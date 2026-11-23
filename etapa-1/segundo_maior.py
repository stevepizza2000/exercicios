# Exercício: encontrar o segundo maior valor distinto de uma lista, sem ordenar


def segundo_maior(numeros):

    maior = None
    segundo = None

    for numero in numeros:
        if maior is None:
            maior = numero
        elif numero == maior:
            pass
        elif numero > maior:
            segundo = maior
            maior = numero
        elif segundo is None or numero > segundo:
            segundo = numero

    return segundo


print(segundo_maior([4, 9, 2, 9, 7]))  # 7
print(segundo_maior([-3, -1, -8]))     # -3
print(segundo_maior([5, 5, 5]))        # None
print(segundo_maior([42]))             # None
print(segundo_maior([]))               # None
print(segundo_maior([9, 7]))           # 7
print(segundo_maior([1, 5]))           # 1
print(segundo_maior([3, 8, 10]))       # 8