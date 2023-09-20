import PySimpleGUI as sg
from numero_dias import diferenca_dias_input

class TelaPython:
    # Definindo a função com as características da janela do meu app, seus botões, entrada e saída de dados.
    def __init__(self):
        layout = [
            [sg.Text("insira as data no formato (dia de mês de ano - dia de mês de ano) ou forneça o nome de um arquivo de texto no qual as datas estejam escritas nesse formato: ", size=(75,0)),sg.Input(size=(70,0),key="entrada")],
            [sg.Button("Enviar Dados", size=(20,0)), sg.Button("Sair", size=(6,0))],
            [sg.Output(size=(40,30))]
        ]
        self.janela = sg.Window("Calculadora de Dias", layout, finalize=True, size=(1200,600))
    
    # Definindo a função com o loop principal do app, a qual roda enquanto o usuário estiver usando a plataforma.
    def Iniciar(self):
        while True:
            event, values = self.janela.read()
            # caso o usuário clique no botão "Sair" ou feche a janela do app, o loop se encerra.
            if event == sg.WINDOW_CLOSED or event == "Sair":
                break
            # Se o usuário clicar no botão "Enviar Dados", deve-se checar se a entrada é um arquivo .txt ou não
            elif event == "Enviar Dados":
                entrada = values["entrada"]
                # Se for um arquivo .txt, abre no modo leitura, lê a primeira linha e usa os dados nela contidos para executar a função que calcula a diferença em dias.
                if entrada.endswith(".txt"):
                    try:
                        with open(entrada, "r") as file:
                            datas = file.readline()
                            print(diferenca_dias_input(datas))
                    # Tratando a exceção em que não se encontra o arquivo especificado pelo usuário
                    except FileNotFoundError:
                        print("Arquivo não encontrado!")
                    # Tratando a exceção na qual o conteúdo do arquivo .txt não está no formato de data especificado
                    except IndexError:
                        print("Conteúdo do arquivo está com o formato incorreto!")
                    # Tratando as demais exceções 
                    except Exception:
                        print(f"Erro ao processar o arquivo: {Exception}")
                # Se não for um arquivo .txt, apenas executa a função que calcula a diferença em dias, usando os dados da entrada como parâmetro.
                else:
                    try:
                        print(diferenca_dias_input(entrada))
                    # Tratando a exceção em que o formato dos dados informados pelo usuário difere do que é pedido na entrada
                    except IndexError:
                        print("Dados fornecidos com o formato incorreto!")
        # Assim que o while passar a ser falso, ou seja, ocorrer algo não mencionado no bloco do while True, a janela se fecha, encerrando o programa.
        self.janela.close()