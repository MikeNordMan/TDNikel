'''Все работает'''


'''Функция находит разницу символов между двух строк 
возвращает разницу в виде строки '''
def getAvailableLetters(s, lettersGuessed):
    k = list(s)

    for c in lettersGuessed:
        try:
            k.remove(c)
        except ValueError:
            pass
    print(''.join(k))
    return ''.join(k)


'''Функция идентифицирует событие'''
def findEvent(findElement, myRow):
    eventsArr = createEventsArr(myRow)
    for i in eventsArr:
        if i == findElement:
            print('Yes', findElement)
            return findElement

'''Функция создает новое значение из полученных 
данных используя формулу вычисления засора'''
def createVal(res,values):
    a = []
    for i in res:
        a.append(values[i])
    if a[1]=='0':
        res = a[0]
    else :
        res = sumP(int(a[0]), int(a[1]))

    return res

'''Функция выводит в поле "засор" вычисленные данные '''
def zasor(findElement,window,values,valuesKeys):

    s = getAvailableLetters(findElement, 'res')
    res = []
    for i in valuesKeys:
        res.append(i + s)
    a = createVal(res, values)
    window[findElement].Update(a)
    return res


'''функция создания массива Событий для вычисления засора'''
def createEventsArr(myRow):
    eventsArr = []
    for i in range(myRow):
        eventsArr.append('res' + str(i))
    print(eventsArr)
    return eventsArr


'''Функция содержит формулу расчета засора '''
def sumP(a, b):  # Функция расчета засора
    c = int(a*(100-b)/100)
    return c