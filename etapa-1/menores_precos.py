# pego o historico passado como parametro
# incio a lista que irá guardar os menores valores
# pego a primeira chave com um for
# com a chave pego a lista com os historicos de valores do produto
# pego os valores dentro da lista e comparo eles até achar o menor

def menores_precos(historico):

    resultado = {} 
    atual = None

    for produto in historico:
        atual = None
        precos_do_produto = historico[produto]
        for preco in precos_do_produto:
            if atual is None or preco < atual:
                atual = preco
                resultado = preco
        
    return resultado



historico = {
    "SSD 1TB": [399.90, 379.90, 389.00],
    "RTX 4060": [1999.00, 1899.90, 1949.00],
    "Monitor 144Hz": [],
}

print(menores_precos(historico))   # {'SSD 1TB': 379.9, 'RTX 4060': 1899.9}
print(menores_precos({}))          # {}