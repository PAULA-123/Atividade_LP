import datetime
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

entrada = input("Digite S para sair ou insira as datas ou o arquivo para o cálculo: ")

def diferenca_dias_input(entrada):

            datas = entrada.split(" - ")
            data_inicial = datas[0]
            data_final = datas[1]

            data_inicial = datetime.strptime(data_inicial, "%d de %B de %Y")

            data_final = datetime.strptime(data_final, "%d de %B de %Y")

            diferenca_de_dias = abs( ( data_final - data_inicial ).days)

            return diferenca_de_dias


if entrada != "S" :
    
    if entrada[-4:]== ".txt":
        # def diferenca_dias_arq():
        #     arquivo = input("Passe um arquivo de texto:")
        #     diferenca_de_dias = 

            # return diferenca_de_dias
        print("é um arquivo")
        entrada = input("Digite S para sair ou insira as datas ou o arquivo para o cálculo: ")
       

    else:
        print(diferenca_dias_input(entrada))
        

else:
    print("Obrigada pela participação!")

# print(diferenca_dias_input())




