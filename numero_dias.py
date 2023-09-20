import datetime
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")

# entrada = input("Digite S para sair ou insira as datas ou o arquivo para o cálculo: ")

#Função que recebe uma string com as datas no formato 'dia de mês de ano - dia de mês de ano' 
#e retorna  a diferença de dias

def diferenca_dias_input(entrada):

            #Divide a string separando as duas datas
            datas = entrada.split(" - ")
            data_inicial = datas[0]
            data_final = datas[1]

            #Converte a primeira data em datetime
            data_inicial = datetime.strptime(data_inicial, "%d de %B de %Y")

            #Converte a segunda data em datetime
            data_final = datetime.strptime(data_final, "%d de %B de %Y")

            #Calcula a diferença de datas e converte em dias
            diferenca_de_dias = abs( ( data_final - data_inicial ).days)

            return diferenca_de_dias


# if entrada != "S" and entrada != "s" :
    
#     if entrada[-4:]== ".txt":
#         # def diferenca_dias_arq():
#         #     arquivo = input("Passe um arquivo de texto:")
#         #     diferenca_de_dias = 

#             # return diferenca_de_dias
#         print("é um arquivo")
        
       

#     else:
#         print(diferenca_dias_input(entrada))
        

# else:
#     print("Obrigada pela participação!")

# print(diferenca_dias_input())




