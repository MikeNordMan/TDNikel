import PySimpleGUI as sg
from window_class import MyWindow
from marki import names


class AddWindow(MyWindow):
    '''Конструктор класса'''
    def __init__(self, mainWindow):
        #super.__init__(mainWindow=mainWindow)
        self.mainWindow =mainWindow
        #self.data = data

    '''Переменные'''
    keyBotton = 'tdn'  # Ключ layout
    myRow = 15  # Возможное колличество строк для появления
    lStrText = 12  # длинна текстового поля
    lenRasdelLine = 75  # Длинна разделительной линии
    openStrAdd = 0  # Колличество открытых строк



    '''Функция Имени'''
    def returnName(self):
        name = 'Окно Поступления'
        return name

    '''Функция Layout Окна'''
    def returnLayout(self):
        '''Часть Layout отвечающая за формирование строки сопроводительной '''
        mol = [[[sg.InputCombo(names, size=(20, 1), key='mar' + str(i + 1), pad=(0, 1)),
                 sg.InputText(key='ves' + str(i + 1), size=(12, 1), pad=(20, 1)),
                 sg.InputText('0', key='-zasor-' + str(i + 1), size=(3, 1), pad=(45, 1)),
                 sg.Text(background_color='#4B8E8D', key='res' + str(i + 1), size=(10, 1), pad=(10, 1),
                         enable_events=True,
                         text_color='white')]] for i in range(self.myRow)]



        layout = self.returnHeader() + [[sg.Column(mol[x], key='col' + str(x + 1), visible=False)] for x in
                          range(self.myRow)] + self.returnColButton() + self.returnExitMesagge()

        # window = sg.Window('Формирование поступления материала', layout, auto_size_text=True, finalize=True)

        # return window
        return layout
    '''Функция темы'''
    def returnTheme(self):
        theme ='LightBrown7'
        return theme