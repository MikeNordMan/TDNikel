import PySimpleGUI as sg
from workWithRow import visibleRow
from workWithRow import visibleRowUn
from check import checkNullStr
from testZasor import zasor, findEvent
from try_check import Check, StrCheck


class MyWindow():
    '''Переменные класса'''
    keys ={'exit': '-exit_', 'print': '-print-', 'delete': '-del-',
           'addStr': '-addStr-', 'offStr': '-offStr-', 'save': '-save-', 'message': '-message-'}
   # message ={'No_numeral': 'Вес указан не верно', 'No_Null': 'Заполните пустые поля','Ok': 'Ok'}
    valuesKeys = ['ves', '-zasor-', 'mar']


    '''Конструктор класса'''
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    '''Используется при создании Layout'''
    def returnColButton(self):
        colButton = [
            [sg.Text('_' * self.lenRasdelLine)],  # Разделительная линия
            [sg.Button('Добавить строку', key=self.keys['addStr'], visible=True),
             sg.Button('Удалить строку', key=self.keys['offStr'], visible=True),
             sg.Button('Сохранить', key=self.keys['save'], visible=True),
             sg.Button('Печать', key=self.keys['print'])],
            [sg.Text('Иформационная строка', key='info', text_color='red', visible=False, pad=(0, 10))]
                    ]
        return colButton

    '''Используется при создании Layout'''
    def returnExitMesagge(self):
        exitMesagge = [
            [sg.Text('jlkjljlkjlkjl', key='txt', size=(40, 2))],
            [sg.Button('Закрыть Окно', key=self.keys['exit'])]
                      ]
        return exitMesagge

    '''Используется при создании Layout'''
    def returnHeader(self):
        heder = [
                [sg.Text('Номер Сопроводительной:', pad=(5, 5)),
                 sg.Text(self.generatorNumDok(self.keyBotton), key='dok', pad=(50, 0))],
                [sg.Text('Дата поступления:', pad=(5, 5)), sg.InputText(key='data', pad=(60, 0), size=(15, 1))],
                [sg.Text('Поставщик:', pad=(5, 5)), sg.InputText(key='post', pad=(100, 0), size=(15, 1))],
                [sg.Text('Транспорт (Марка, номер)', pad=(5, 5)), sg.InputText(key='auto', pad=(15, 5), size=(15, 1))],
                [sg.Text('_' * self.lenRasdelLine)],  # Разделительная линия
                [sg.Text('Наименование', pad=(20, 5), size=(self.lStrText, 1)),
                sg.Text('Вес Нетто (кг)', pad=(45, 5), size=(10, 1)),
                sg.Text('Засор ( % )', pad=(1, 5), size=(self.lStrText, 1)),
                sg.Text('Вес Брутто (кг)', pad=(1, 5), size=(self.lStrText, 1))]
                ]
        return heder

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
        windowClass = sg.Window(self.returnName(), self.returnLayout())
        self.controlWindow(windowClass)

    '''Функция контроля окна'''
    def controlWindow(self, windowClass):
        while True:
            event, values = windowClass.read()

            if event in (None, self.keys['exit']):
                self.colseWindow(self.mainWindow, windowClass)
                break
            '''Печать'''
            if event == self.keys['print']:
               print(values)
               self.myPrint()

            if event == self.keys['delete']:
               self.myDelete()

            '''Открытие новой строки'''
            if event == self.keys['addStr']:
                chStr = StrCheck(windowClass, values, self.valuesKeys, self.openStrAdd)
                self.addStr(chStr.checkObject(), windowClass)

            '''Засор'''
            if event == findEvent(event, self.myRow):
                print('Работаем')
                zasor(event, windowClass, values, self.valuesKeys)



            if event == self.keys['offStr']:
               self.openStrAdd =self.offStr(self.openStrAdd, windowClass)


            if event == self.keys['save']:
               self.mySave()

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

    '''Добавление строки'''

    def addStr(self, message, windowsClass):
        print('Добавление строки')
        if message == 'Ok':
            self.openStrAdd = visibleRow(self.openStrAdd, self.myRow, windowsClass)
            return self.openStrAdd
        else:
            self.openStrAdd = self.openStrAdd-1
            self.openStrAdd = visibleRow(self.openStrAdd, self.myRow, windowsClass)
            return self.openStrAdd




    '''Удаление строки'''
    def offStr(self, openStrAdd, windowsClass):
        print('Удаление строки')
        openStrAdd = visibleRowUn(openStrAdd, windowsClass)
        return openStrAdd

    '''Функция Сохранение'''
    def mySave(self):
        print('Сохранено')

    def generatorNumDok(self, numDok):
        if numDok == 'tdn':
            return numDok
        if numDok == 'real':
            return numDok

    '''Генератор сообщений об ошибке'''
    def mesaggeMistake(self, message, windowsClass):
        if self.message.get(message) == 'Ok':
            windowsClass[self.keys['message']].Update(visible=False)
            return 'Ok'
        else:
            print('Ошибка код:', message)
            mesageMistake = self.message.get(message)
            windowsClass[self.keys['message']].Update(mesageMistake, visible=True)

    '''Тестовая функция засора'''

    def testZasor(self, openStrAdd):
        c = 'res' + str(openStrAdd)
        return c


