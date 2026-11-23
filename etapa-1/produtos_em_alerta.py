# a função recebe as listas pré definidas de precos atuais e alvos
# eu desmembro os alvos para comparar as chaves com os valores delas
# caso eu não tenha o preço atual do produto eu não o adiciono na lista para não ter probllema de key error
# coso não tenha alvos eu retorno uma lista vazia
# retorna a lista com os nomes dos produtos

def produtos_em_alerta(precos, alvos):
    
    resultado = []

    for alvo in alvos:
        if alvo in precos and precos[alvo] <= alvos[alvo]:
            resultado.append(alvo)
        
    return resultado

precos = {"RTX 4060": 1899.90, "Ryzen 5 7600": 1149.00, "SSD 1TB": 379.90}
alvos = {"RTX 4060": 1700.00, "SSD 1TB": 400.00, "Ryzen 5 7600": 1149.00, "Monitor 144Hz": 900.00}


print(produtos_em_alerta(precos, alvos))   # ['SSD 1TB', 'Ryzen 5 7600']
print(produtos_em_alerta(precos, {}))      # []