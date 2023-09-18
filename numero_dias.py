import datetime

from datetime import datetime

import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

# #data final 
# d2 = datetime.strptime("2017-05-05", "%Y-%m-%d")

# d1 = datetime.strptime("2017-05-01", "%Y-%m-%d")

# print(quant_dias = abs( ( d2 - d1 ).days))

def diferenca_dias_input():
    data_inicial = input("Digite a data inicial: ")
    data_final = input("Digite a data final: ")

    data_inicial = datetime.strptime(data_inicial, "%d de %B de %Y")

    data_final = datetime.strptime(data_final, "%d de %B de %Y")

    diferenca_de_dias = abs( ( data_final - data_inicial ).days)

    return diferenca_de_dias

print(diferenca_dias_input())

# def diferenca_dias_arq():
#     arquivo = input("Passe um arquivo de texto:")
#     diferenca_de_dias = 

#     return diferenca_de_dias


"""

def diferenca_dias():
    datas = input("Digite a data inicial e a data final: ")27 de março de 2023 - 18 de agosto de 2021
    
    data_final = datas.strip("-")


    # data = datetime.strptime(datas, "%Y-%m-%d")

    # diferenca_de_dias = abs( (datas).days)

    return data_final

print(diferenca_dias())

"""

