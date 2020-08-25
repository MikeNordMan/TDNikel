import PySimpleGUI as sg
from mainWindow import openMineWindow

layout = [
          [sg.Text('Начало работы приложеия')],
          [sg.Button('Поехали', key='-ok-'),sg.Button('Выход', key='-exit-')]
         ]


firstWindow = sg.Window('Первое окно', layout, size=(200, 100))


while True:
    event, values = firstWindow.read()


    if event in (None, '-exit-'):
        break

    if event =='-ok-':
        firstWindow.close()
        openMineWindow()

firstWindow.close()