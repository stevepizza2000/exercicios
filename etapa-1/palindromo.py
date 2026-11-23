# Exercício: verificar se uma palavra é palíndromo (técnica de dois ponteiros)
# Observação: versão corrigida com ajuda do mentor (índice vs. valor, condição do while)


def eh_palindromo(palavra):
    inicio = 0                    # índice da primeira caixa (número)
    fim = len(palavra) - 1        # índice da última caixa (número)

    while inicio < fim:           # os dedos ainda não se cruzaram?
        if palavra[inicio] != palavra[fim]:   # aqui abrimos as caixas
            return False          # letras diferentes: não é palíndromo
        inicio += 1               # dedo da esquerda anda para a direita
        fim -= 1                  # dedo da direita anda para a esquerda

    return True                   # chegou aqui sem achar diferença


print(eh_palindromo("radar"))  # True
print(eh_palindromo("abba"))   # True
print(eh_palindromo("abca"))   # False