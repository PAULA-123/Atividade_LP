import datetime

from datetime import datetime


# #data final 
# d2 = datetime.strptime("2017-05-05", "%Y-%m-%d")

# d1 = datetime.strptime("2017-05-01", "%Y-%m-%d")

# print(quant_dias = abs( ( d2 - d1 ).days))
"""
def diferenca_dias():
    data_inicial = input("Digite a data inicial: ")
    data_final = input("Digite a data final: ")

    data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")

    data_final = datetime.strptime(data_final, "%Y-%m-%d")

    diferenca_de_dias = abs( ( data_final - data_inicial ).days)

    return diferenca_de_dias

print(diferenca_dias())
"""

def diferenca_dias():
    datas = input("Digite a data inicial e a data final: ")
    

    data = datetime.strptime(datas, "%Y-%m-%d")

    diferenca_de_dias = abs( ( data_final - data_inicial ).days)

    return diferenca_de_dias

print(diferenca_dias())



