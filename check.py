def checkNullStr(openStrAdd, values):
    print('Открыта строка: ', openStrAdd)
    if openStrAdd != 0:
        control = objectCreate(openStrAdd)
        if nullControll(values, control) == 'Ok':
            if numeralControl(values, control) == 'No_numeral':
                message = 'No_numeral'
                return message
            else:
                message = 'Ok'
                return message
        else:
            message = 'No_Null'
            return message
    else:
        message = 'Ok'
        return message

'''Функция создает объекты для проверки'''
def objectCreate(openStrAdd):
    arrObjectControl = []
    nameObjContr =['mar', 'ves']
    for i in nameObjContr:
        arrObjectControl.append(i+str(openStrAdd))
    print('Созданный объект контроля', arrObjectControl)
    return arrObjectControl

'''Проверка на зачение Null'''
def nullControll(valuesDict, arrObjectControl):
    for i in arrObjectControl:
         control = valuesDict.get(i)
         if control == '':
             print('Полее', control)
             print('Не заполнено поле:', i)
             checkFlag = 'No_Null'
             return checkFlag
         else:
             checkFlag = 'Ok'
             return checkFlag

'''Проверка на цифру'''
def numeralControl(valuesDict, arrObjectControl):
    if valuesDict.get(arrObjectControl[1]).isdigit() ==True:
        checkFlag = 'Ok'
        return checkFlag
    else:
        checkFlag = 'No_numeral'
        return checkFlag



