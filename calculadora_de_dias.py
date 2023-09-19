import PySimpleGUI as sg
from numero_dias import diferenca_dias_input

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text("Digite S para sair, insira as data no formato (dia de mês de ano - dia de mês de ano) ou forneça um arquivo de texto com as datas nesse formato: ", size=(75,0)),sg.Input(size=(70,0),key="entrada")],
            [sg.Button("Enviar Dados", size=(20,0)), sg.Button("Sair", size=(6,0))], #adicionando um botão para sair
            [sg.Output(size=(40,30))]
        ]
        self.janela = sg.Window("Calculadora de Dias", layout, finalize=True, size=(1200,600))
        
    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break
            elif event == "Enviar Dados":
                entrada = values["entrada"]
                if entrada.endswith(".txt"):
                    try:
                        with open(entrada, "r") as file:
                            datas = file.readline()
                            print(diferenca_dias_input(datas))
                    except FileNotFoundError:
                        print("Arquivo não encontrado!")
                    except Exception:
                        print(f"Erro ao processar o arquivo: {Exception}")
                else:
                    print(diferenca_dias_input(entrada))
        self.janela.close()