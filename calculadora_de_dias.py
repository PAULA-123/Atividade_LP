import PySimpleGUI as sg
from numero_dias import diferenca_dias_input

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text("Digite S para sair ou insira as data no formato (dia de mês de ano - dia de mês de ano): ", size=(65,0)),sg.Input(size=(60,0),key="datas")],
            [sg.Button("Enviar Dados", size=(20,0)), sg.Button("Sair", size=(6,0))], #adicionando um botão para sair
            [sg.Output(size=(30,20))]
        ]
        self.janela = sg.Window("Calculadora de Dias", layout, finalize=True)
        
    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break
            elif event == "Enviar Dados":
                datas = values["datas"]
                print(diferenca_dias_input(datas))
        self.janela.close()