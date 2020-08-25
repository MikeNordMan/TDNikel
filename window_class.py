import PySimpleGUI as sg

class MyWindow():
    '''Переменные класса'''
    keys ={'exit': '-exit_', 'print': '-print-', 'delete': '-del-'}

    '''Конструктор класса'''
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow


    '''Функция Layout Окна'''
    def returnLayout(self):
        layout = [
                  [sg.Text('Тут LAYOUT окна')],
                  [sg.Button('Выход', key=self.keys['exit'])]
                 ]
        return layout
    '''Функция темы'''
    def returnTheme(self):
        theme = ''
        return theme

    '''Функция Имени'''
    def returnName(self):
        name = 'Окно'
        return name

    '''Основная функция класса'''
    def startWindow(self):
        sg.theme(self.returnTheme())
        windowClass =sg.Window(self.returnName(), self.returnLayout(), size=(300, 200))
        self.controlWindow(windowClass)

    '''Функция контроля окна'''
    def controlWindow(self, windowClass):
        while True:
            event, values = windowClass.read()

            if event in (None, self.keys['exit']):
                self.colseWindow(self.mainWindow, windowClass)
                break
            if event == self.keys['print']:
               self.myPrint()

            if event == self.keys['delete']:
               self.myDelete()


    '''Функция закрытия окна'''
    def colseWindow(self, mainWindow, windowClass):
        windowClass.close()
        mainWindow.UnHide()

    '''Функция Печати '''
    def myPrint(self):
        print('Получилось, Работает')

    '''Функция Удаление'''
    def myDelete(self):
        print('Удаление')
