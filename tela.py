import PySimpleGUI as sg

class TelaPyhton:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome', size=(10,0)),sg.Input(size=(100,100), key='nome')],
            [sg.Text('Naturalidade', size=(10,0)), sg.Input(size=(100,100), key='naturalidade')],
            [sg.Text('Qual cidade?')],
            [sg.Checkbox('Altos', key='altos'), sg.Checkbox('Teresina', key='teresina'), sg.Checkbox('Timon', key='timon')],
            [sg.Text('Aceita cajuina?')],
            [sg.Radio('Sim', 'cajuina', key='aceitacajuina'),sg.Radio('Não','cajuina', key='naoaceitacajuina')],            
            [sg.Button('Enviar Dados')]
        ]
        # Janela
        janela = sg.Window("Primeira interface").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']
        naturalidade = self.values['naturalidade']
        aceita_altos = self.values['altos']
        aceita_teresina = self.values['teresina']
        aceita_timon = self.values['timon']
        aceita_cajuina = self.values['aceitacajuina']
        nao_aceita_cajuina = self.values['naoaceitacajuina']
        print(f'nome: {nome}')
        print(f'idade: {naturalidade}')
        print(f'aceita Altos: {aceita_altos}')
        print(f'aceita Teresina: {aceita_teresina}')
        print(f'aceita Timon: {aceita_timon}')
        print(f'Aceita cajuina: {aceita_cajuina}')
        print(f'Não aceita cajuina: {nao_aceita_cajuina}')
        #print(self.values)    

tela = TelaPyhton()
tela.Iniciar()