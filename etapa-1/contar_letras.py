# Exercício: contar quantas vezes uma letra aparece em uma palavra


def contar_letras(palavra, letra):
    i = 0
    fim = len(palavra) - 1
    contador = 0

    while i <= fim:
        if palavra[i] == letra:
            contador += 1

        i += 1

    return contador


print(contar_letras("bbb", "b"))      # 3
print(contar_letras("banana", "a"))   # 3, caso comum
print(contar_letras("python", "z"))   # 0, a letra não aparece
print(contar_letras("", "a"))         # 0, palavra vazia
print(contar_letras("arara", "a"))    # 3, a letra está nas duas pontas
print(contar_letras("Banana", "b"))   # 0, maiúscula é diferente de minúscula