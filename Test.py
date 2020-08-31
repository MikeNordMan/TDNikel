def n1():
    print('первая функция')
    return 'No'

def n2():
    print('вторая функция')
    return 'No'

def n3():
    print('третья функция')
    return 'No'


arr = [n1(), n2(), n3()]

a = []
for i in arr:
    a.append(i)
if 'Yes' in a:
    print('есть')
else:
    print('нет')