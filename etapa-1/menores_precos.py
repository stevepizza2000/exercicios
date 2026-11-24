# para cada produto do histórico:
# pego a lista de preços do produto
# começo sem nenhum menor (None)          ← dentro do for de fora!
# para cada preço da lista:
# se ainda não tenho menor OU o preço é menor que o que tenho:
# esse preço passa a ser o menor
# se encontrei algum menor (a lista não estava vazia):
# guardo no resultado: produto → menor
# retorno o resultado

def menores_precos(historico):

    resultado = {}

    for produto in historico:
        precos_do_produto = historico[produto]
        menor = None
        for preco in precos_do_produto:
            if menor is None or preco < menor:
                menor = preco
        
        if menor is not None:   
            resultado[produto] = menor
    
    return resultado
        



historico = {
    "SSD 1TB": [399.90, 379.90, 389.00],
    "RTX 4060": [1999.00, 1899.90, 1949.00],
    "Monitor 144Hz": [],
}

print(menores_precos(historico))   # {'SSD 1TB': 379.9, 'RTX 4060': 1899.9}
print(menores_precos({}))          # {}