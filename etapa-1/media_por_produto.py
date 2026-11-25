# inicializo o dicionario vazio
# para cada produto do histórico
# pego a lista de preços do produto
# pego o tamanho da lista de precos
# começo com uma media 0
# para cada preço da lista
# somo todos os precos na lista_precos
# se tamanho for diferente de 0
# media final igual a media dividido por tamanho
# guardo o resultado do produto no dicionario e arredondo para 2 casas depois da ","
# retorno resultado

def media_por_produto(historico):

    resultado = {}

    for produto in historico:
        lista_precos = historico[produto]
        tamanho = len(lista_precos)
        media = 0
        for preco in lista_precos:
            media += preco
        if tamanho != 0:
            media_final = media / tamanho
            resultado[produto] = round(media_final, 2)


    return resultado

historico = {
    "SSD 1TB": [399.90, 379.90, 389.00],
    "RTX 4060": [1999.00, 1899.90, 1949.00],
    "Monitor 144Hz": [],
}

print(media_por_produto(historico))   # {'SSD 1TB': 389.6, 'RTX 4060': 1949.3}
print(media_por_produto({}))          # {}