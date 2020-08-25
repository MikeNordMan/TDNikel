import PySimpleGUI as sg
from window_class import MyWindow


class ReworkWindow(MyWindow):

    '''Конструктор класса'''
    def __init__(self, mainWindow):
        #super.__init__(mainWindow=mainWindow)
        self.mainWindow =mainWindow
        #self.data = data

    '''Функция Имени'''
    def returnName(self):
        name = 'Окно переработки'
        return name

    '''Функция Layout Окна'''
    def returnLayout(self):
        layout = [
            [sg.Text('Переработка')],
            [sg.Button('Удаление', key=self.keys['delete'])],
            [sg.Button('Выход', key=self.keys['exit'])]
        ]
        # # return layout
        # sg.theme(self.theme[2])
        # heder = [[sg.Text('Акт переработки № '),sg.Text(self.generatorNumDok(self.keyButton), key='dok')],
        #          [sg.Text('Материал подлежащий переработке:')],
        #          [sg.Text('Вид Переработки'), sg.InputCombo(moveMetal, size=(20, 1), key='moveM')],
        #          [sg.Text('Марка'), sg.Text('Вес Нетто (кг)')]
        #         ]
        # heder1 =[[sg.Text('Материал образованный в результате переработки:')],
        #          [sg.Text('Марка'), sg.Text('Вес Нетто (кг)')]
        #         ]
        #
        # mol = [[[sg.InputCombo(names, size=(20, 1), key='mar' + str(i + 1), pad=(0, 1)),
        #          sg.InputText(key='vesN' + str(i + 1), size=(12, 1), pad=(20, 1))
        #          ]] for i in range(self.myRow)]
        #
        # nol = [[[sg.InputCombo(names, size=(20, 1), key='1mar' + str(i + 1), pad=(0, 1)),
        #          sg.InputText(key='1vesN' + str(i + 1), size=(12, 1), pad=(20, 1))
        #          ]] for i in range(self.myRow1)]
        #
        # line =[[sg.Button('Добавить строку', key='-addStrP-', visible=True),
        #         sg.Button('Удалить строку', key='-offStrP-', visible=True)],
        #         [sg.Text('_' * self.lenRasdelLine)]]
        #
        # line1=[[sg.Button('Добавить строку', key='-addStrP1-', visible=True),
        #         sg.Button('Удалить строку', key='-offStrP1-', visible=True)],
        #         [sg.Text('_' * self.lenRasdelLine)]]
        #
        # colButton = [[sg.Button('Закрыть окно', key='-close-'), sg.Button('Сохранить', key='-save-')]]
        #
        # layout = heder + [[sg.Column(mol[x], key='col'+ str(x+1), visible=False)] for x in range(Post.myRow)] + line\
        #          + heder1+ [[sg.Column(nol[i], key='1col' + str(i + 1), visible=False)] for i in range(Post.myRow1)]\
        #          + line1 + colButton
        # return layout


    '''Функция темы'''
    def returnTheme(self):
        theme ='DarkBlue'
        return theme