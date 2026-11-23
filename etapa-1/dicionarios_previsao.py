# primeiro a palavra é colocada na função
# inicio o dicionario vazio
# percorro as letras na palavra
# se a letra já estiver no dicionario o valor dela aumenta em 1
# se não ela é adicionada com o valor inicial 1
# função retorna o dicionario


def contar_frequencia(palavra):
    
    dicionario = {}

    for letra in palavra:
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1
    
    return dicionario

    

print(contar_frequencia("banana"))   # {'b': 1, 'a': 3, 'n': 2}
print(contar_frequencia("arara"))    # {'a': 3, 'r': 2}
print(contar_frequencia(""))         # {}