'''Класс Check и его модификации служат для обработки ошибок событий'''


import PySimpleGUI as sg

class Check(object):

    '''Конструктор'''
    def __init__(self, window, values, valuesKeys):
        self.window = window
        self.values = values
        self.valuesKeys = valuesKeys

    '''Переменные класса'''
    checkFlagDict = {'Ok': 'Ok', 'No_Null': 'Заполните пустые поля', '': '', }
    methodControl = []

    def createObject(self):
        print('Объект для входа', self.values)

    '''Реакция на положительный Флаг'''
    def answerPositiveFlag(self, chekFlag):
        self.window['info'].Update(self.checkFlagDict[chekFlag], visible=True)

    '''Реакция на отрицательный Флаг'''
    def answerNegativeFlag(self):
        self.window['info'].Update(visible=False)


class StrCheck(Check):
    '''Конструктор'''

    def __init__(self, window, values, valuesKeys, openStrAdd):
        super().__init__(window, values, valuesKeys)
        self.openStrAdd = openStrAdd

    '''Переменные класса'''
    # methodControl = [nullControll(),]

    def checkObject(self):
        flagM =[]
        print('Подкласс, Объект для входа', self.values)
        # print('OpenStrAdd', self.openStrAdd)
        # print('valuesKeys', self.valuesKeys)
        self.methodControl.append(self.nullControll())

        for i in self.methodControl:
            flagM.append(i)

        print('Результат vj', flagM)

        if flagM[len(flagM)-1] == 'No' :
            return 'No'
        else:
            return 'Ok'



    def createCheckArr(self):
        checkArr = []
        for i in self.valuesKeys:
            checkArr.append(i+str(self.openStrAdd))
        print('Результат функции "createCheckArr": ', checkArr)
        return checkArr

    '''Проверка на зачение Null'''
    def nullControll(self):
        flag =[]
        print('check:', self.createCheckArr() )
        for i in self.createCheckArr():
            control = self.values.get(i)
            if control == '':
                # print('Поле', control)
                # print('Не заполнено поле:', i)
                flag.append('No')
            else:
                flag.append('Yes')

        #print('NullControll:', flag)
        if 'No' in flag:
            self.answerPositiveFlag('No_Null')
            return 'No'
        else:
            self.answerNegativeFlag()
            return 'Ok'

    # '''Переменные класса'''
    # methodControl = [self.nullControll()]

#
# '''Тест'''
# val = {'data': '', 'post': '', 'auto': '', 'mar1': '', 'ves1': '', '-zasor-1': '0', 'mar2': '', 'ves2': '', '-zasor-2': '0', 'mar3': '', 'ves3': '', '-zasor-3': '0', 'mar4': '', 'ves4': '', '-zasor-4': '0', 'mar5': '', 'ves5': '', '-zasor-5': '0', 'mar6': '', 'ves6': '', '-zasor-6': '0', 'mar7': '', 'ves7': '', '-zasor-7': '0', 'mar8': '', 'ves8': '', '-zasor-8': '0', 'mar9': '', 'ves9': '', '-zasor-9': '0', 'mar10': '', 'ves10': '', '-zasor-10': '0', 'mar11': '', 'ves11': '', '-zasor-11': '0', 'mar12': '', 'ves12': '', '-zasor-12': '0', 'mar13': '', 'ves13': '', '-zasor-13': '0', 'mar14': '', 'ves14': '', '-zasor-14': '0', 'mar15': '', 'ves15': '', '-zasor-15': '0'}
# win = 'Window'
# oSA = 1
# valKey = ['mar', 'ves', '-zasor-']
#
# chStr = StrCheck(win, val, valKey, oSA)
# chStr.createObject()