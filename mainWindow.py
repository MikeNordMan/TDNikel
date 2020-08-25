import PySimpleGUI as sg
from window_class import MyWindow
from addWindow import AddWindow
from reworkWindow import ReworkWindow
from realWindow import RealWindow

def prepareOpenWidow(activate, window):
    activate = True
    window.Hide()

def openMineWindow():


    layout=[
            [sg.Text('Главная страница Приложения')],
            [sg.Button('Окно Поступления', key='-add-')],
            [sg.Button('Окно Реализации', key='-real-')],
            [sg.Button('Окно Переработки', key='-rework-')],
            [sg.Button('Выход', key='-exit-')]
           ]

    mainWindow = sg.Window('Главное окно', layout, size=(250, 250))

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