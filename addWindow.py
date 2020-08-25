import PySimpleGUI as sg
from window_class import MyWindow


class AddWindow(MyWindow):
    '''Конструктор класса'''
    def __init__(self, mainWindow):
        #super.__init__(mainWindow=mainWindow)
        self.mainWindow =mainWindow
        #self.data = data

    '''Функция Имени'''
    def returnName(self):
        name = 'Окно Поступления'
        return name

    '''Функция Layout Окна'''
    def returnLayout(self):
        layout = [
            [sg.Text('Поступление')],
            [sg.Button('Печать', key=self.keys['print'])],
            [sg.Button('Выход', key=self.keys['exit'])]
        ]
        return layout

    '''Функция темы'''
    def returnTheme(self):
        theme ='DarkBlue10'
        return theme