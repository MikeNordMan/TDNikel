import PySimpleGUI as sg
import datetime

from addWindow import AddWindow
from reworkWindow import ReworkWindow
from realWindow import RealWindow

now = datetime.datetime.now() # Получаем текущую дату
now = now.strftime('%d.%m.%Y')

def prepareOpenWidow(activate, window):
    activate = True
    window.Hide()

'''Функция формирующая Остатки на складе '''
def ost():
    data ='Данные по Складу'
    return data

'''Функция Формирования Журнала Событий'''
def ivetLog(nowDate): # Вход сегодняшняя дата
    data = 'Список Событий'
    return data


def openMineWindow():

    keys = {'add': '-add-', 'real': '-real-', 'rework': '-rework-'}

    '''Цвет темы'''
    sg.theme('LightPurple')

    layout = [
              [sg.Frame('', [[sg.Text('Остатки на складе', size=(30, 1))],
              [sg.Multiline(default_text=ost(), key='depot', size=(35, 20))]]),
              sg.Frame('', [[sg.Button('Поступление', key=keys['add'], size=(10, 1))],
                       [sg.Button('Реализация', key=keys['real'], size=(10, 1))],
                       [sg.Button('Переработка', key=keys['rework'], size=(10, 1))]]),

              sg.Frame('', [[sg.Text('Дата'), sg.InputText(now, key='nowDate', size=(10, 1))],
                       [sg.Listbox(values=ivetLog(now), key='eventLog', size=(20, 19))],
                       [sg.Button('Редактировать', key='-edit-', size=(20, 1))]])],

              [sg.Text('_' * 90)],
              [sg.Button('Exit', key='-exit-')]  # Посмотреть tooltip!!!
             ]

    mainWindow = sg.Window('Main window', layout)

    '''Переменные активности'''
    addWindow_active = False
    realWindow_active = False
    reworkWindow_active = False

    while True:
        event, values = mainWindow.read()

        if event in (None, '-exit-'):
            break

        if event =='-add-' and not addWindow_active:
            prepareOpenWidow(addWindow_active, mainWindow)
            w = AddWindow(mainWindow)
            w.startWindow()
            addWindow_active = False


        if event =='-real-' and not realWindow_active:
            prepareOpenWidow(realWindow_active,mainWindow)
            w = RealWindow(mainWindow)
            w.startWindow()
            realWindow_active = False


        if event =='-rework-' and not reworkWindow_active:
            prepareOpenWidow(realWindow_active,mainWindow)
            w = ReworkWindow(mainWindow)
            w.startWindow()
            realWindow_active =False

    mainWindow.close()