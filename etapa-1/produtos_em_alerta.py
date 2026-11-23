# a função recebe os preços e alvos como paramentros
# inicio uma lista vazia para adicionar os nomes dos produtos que estão com o preço abaixo ou igual o alvo
# procuro na lista de preços alvos produto por produto
# checo se a chave do produto atual existe em precos e se o valor do produto está menor ou igual ao alvo
# caso passe nos testes eu adiciono na lista
# retorno o resultado


def produtos_em_alerta(precos, alvos):
    
    resultado = []

    for produto in alvos:
        if produto in precos and precos[produto] <= alvos[produto]:
            resultado.append(produto)
        
    return resultado

precos = {"RTX 4060": 1899.90, "Ryzen 5 7600": 1149.00, "SSD 1TB": 379.90}
alvos = {"RTX 4060": 1700.00, "SSD 1TB": 400.00, "Ryzen 5 7600": 1149.00, "Monitor 144Hz": 900.00}


print(produtos_em_alerta(precos, alvos))   # ['SSD 1TB', 'Ryzen 5 7600']
print(produtos_em_alerta(precos, {}))      # []