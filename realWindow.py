import PySimpleGUI as sg
from window_class import MyWindow


class RealWindow(MyWindow):

    '''Конструктор класса'''
    def __init__(self, mainWindow):
        #super.__init__(mainWindow=mainWindow)
        self.mainWindow =mainWindow
        #self.data = data

    '''Функция Имени'''
    def returnName(self):
        name = 'Окно реализации'
        return name

    '''Функция Layout Окна'''
    def returnLayout(self):
        layout = [
            [sg.Text('Реализация')],
            [sg.Button('Печать', key=self.keys['print'])],
            [sg.Button('Удаление', key=self.keys['delete'])],
            [sg.Button('Выход', key=self.keys['exit'])]
        ]
        return layout

    '''Функция темы'''
    def returnTheme(self):
        theme ='BlueMono'
        return theme