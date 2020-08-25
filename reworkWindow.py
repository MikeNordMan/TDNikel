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
        return layout

    '''Функция темы'''
    def returnTheme(self):
        theme ='DarkBlue'
        return theme