import PySimpleGUI as sg

class Check(object):

    '''Конструктор'''
    def __init__(self, window, values):
        self.window = window
        self.values = values

    def createObject(self):
        print(self.values)
