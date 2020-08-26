'''Нихрена не получилось'''


def zasor(values, openStrAdd):
    ob = objectCreate(openStrAdd)
    a = int(values.get(ob[0]))
    print(a)
    b = int(values.get(ob[1]))
    print(b)
    print(a+b)
    if b==0:
        res = str(a)
        return res
    else:
        res =str(sumP(a,b))

    #res =100
        return res

'''Функция создает объекты для вычисления засора'''
def objectCreate(openStrAdd):
    arrObject = []
    nameObj =['ves', '-zasor-']
    for i in nameObj:
        arrObject.append(i+str(openStrAdd))
    print('Созданный объект', arrObject)
    return arrObject

def sumP(a, b):  # Функция расчета засора
    c=a*(100-b)/100
    return c