# <Tela@MDFloatLayout>:
    # MDFlatButton:
    #     text: "Botão 1"
    #     size_hint_x: .2
    #     size_hint_y: .1
    #     pos_hint:{"center_x":.5, "center_y":.5}
    #     font_size: "30sp"
    #     theme_text_color:"Custom"
    #     text_color: 0.2,0.5,0.5,1
    #     line_color: 0.2,1,0,1

    # MDLabel:
    #     text: "0"
    #     size_hint_x: .3
    #     size_hint_y: .1
    #     font_size: "150sp"
    #     pos_hint:{"center_x": .6, "center_y":.7}


# Tela:

import PySimpleGUI as sg
from numero_dias import diferenca_dias_input

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text("Digite S para sair ou insira as datas ou o arquivo para o cálculo: ", size=(50,0)),sg.Input(size=(55,0))],
            [sg.Button("Enviar Dados", size=(6,0))]
        ]
        janela = sg.Window("Data inicial e Data final").layout(layout)
        #Extrair os dados da tela
        self.button, self.values = janela.Read()
        self.janela = sg.Window("Data inicial e Data final").layout(layout)
        if entrada != "S" and entrada != "s" :
    
            if entrada[-4:]== ".txt":
                print("é um arquivo")
            else:
                print(diferenca_dias_input(self.button, self.values == janela.Read()))
                    
        else:
            print("Obrigada pela participação!")
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
        print(self.values)