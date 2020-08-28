'''Нихрена не получилось'''
'''Попытка 2'''






def getAvailableLetters(s, lettersGuessed):
    k = list(s)

    for c in lettersGuessed:
        try:
            k.remove(c)
        except ValueError:
            pass
    print(''.join(k))
    return ''.join(k)

def mySumm(a,b):
    c =int(a) + int(b)
    return str(c)

def findEvent(findElement,myRow):

    eventsArr=createEventsArr(myRow)
    for i in eventsArr:
        if i == findElement:
            print('Yes', findElement)
            return findElement

def createVal(res,values):
    a = []
    for i in res:
        a.append(values[i])
    res = mySumm(a[0],a[1])
    return res

def abcd(findElement,window,values):
    print('Функция ABCD - запущена')
    s = getAvailableLetters(findElement, 'vesN')
    res = []
    for i in valuesKeys:
        res.append(i + s)
    a = createVal(res,values)
    window[findElement].Update(a)
    return res


'''функция создания массива Событий для вычисления засора'''
def createEventsArr(myRow):
    eventsArr = []
    for i in range(myRow):
        eventsArr.append(myRow + str(i))
    print(eventsArr)
    return eventsArr



def sumP(a, b):  # Функция расчета засора
    c=a*(100-b)/100
    return c