# zip(iterables) - она соединяет каждый элемент итерируемых обьектов между собой в тип данных tuple и возвращает итератор

# ls1 = [1,2,3]
# ls2 = [100, 200, 300, 123]
# ls3 = ['Hello', 'world', 'John']
# result = zip(ls1, ls2, ls3)
# print(result)
# for x in result:
#     print(x)
# ----------------------------------
# all(), any()

# all(iterable) - возвращает True, если все элементы итерируемого обьекта истина, иначе False

# ls = [[1, 2], -5, 'stroka', 1]
# print(all(ls))

# ip1 = '10.255.12.155'
# ip2 = '10.255.1y.123'

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)
# result2 = all(x.isdigit() for x in ip2.split('.'))
# print(result2)

# any - возвращает True, если хотя бы один элемент истина.

# ls = [0, 0, '', None, [], 1]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Enter a command: ')
# if any(x in command for x in ignore):
#     raise Exception('You don\'t have permmissions!')

# print('ok')

# Анонимные функции - lambda(обычные функции тольок без названия)
# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение

# def sum_of_args(a, b):
#     return a + b

# print(sum_of_args(6, 5))

# func = lambda a: a+10
# print(func(15))

# def myFunc(n):
#     def result(num):
#         return num * n
#     return result

# myDoubler = myFunc(2) #-> n = 2
# myTripler = myFunc(3) #-> n = 3

# print(myDoubler(50)) #-> num = 50
# print(myDoubler(76))
# print(myDoubler(150))

# print(myTripler(55)) #-> num = 55

# def myFunc(n):
#     return lambda num: num * n

# res= myFunc(4)
# print(res(10))

# ____________________________________________________________________________________

# map(function,iterable) -> применяет функцию которую мы передаем ко всем элементам iterable
# ls = ['one','two','three','Anvar','King']
# res = list(map(str.upper, ls))
# print(res)

# res = []
# for x in ls: 
#     res.append(x.upper())
# print(res)

# names = ['John', 'Sultan','Anvar','Din','Sam']
# res = list(map(
#     lambda name: f'hello mr/mrs {name}!,',
#     names
# ))
# print(res)


# dict_ = {1: 2, 3: 4, 5: 6}
# #  --------> {1:'2', 3: '4',5: '6'}
# print(dict_)
# res = dict(map(
#     lambda x: (x[0], str(x[1])), dict_.items())
#     )

# print(res)

# ___________________________________________________________________________________

# filter(function, iterable) -> применяет ко всем элементам iterable функцию 
# которую мы передаем и возвращает итератор с теми элементами для которых функция вернула True


# есть ли в списке цифры
# ls = ['one','two', '', 'list', '100','12', 'Din']


# 1)
# res = []
# for x in ls: 
#     if x.isdigit():
#         res.append(x)
# print(res)

# 2)
# res = list(filter(str.isdigit, ls))
# print(res)


# если слово больше 5 
# ls = ['John', 'codify', 'aibek','ana','bootcamp','Kyrgyzstan','mountains']

# res = list(filter(
#     lambda x: len(x)>5, ls
# ))
# print(res)


# вытащить языки которые он знает на отлично с баллом 9 и 10 

# ls = [
#     {'name': 'Python','point': 10},
#     {'name': 'C++','point':6},
#     {'name': 'JS','point': 8},
#     {'name': 'JAVA','point': 3},
#     {'name': 'C#','point': 9},

# ]

# res = list(filter(
#     lambda dict_: dict_['point']>8, ls 
# ))
# print(res)


# users = [
#     {'username': 'Din', 'comments': ['I love u!', 'so georgous!']},
#     {'username': 'Raychel' , 'comments': []},
#     {'username': 'Steven', 'comments': ['Bishkek', 'Python']},
#     {'username': 'Sam', 'comments': []},
#     {'username': 'Kira', 'comments': ['The best post!']}
#     ]

# active = list(filter(
#     lambda obj: obj['comments'], users 
# ))
# inactive = list(filter(
#     lambda obj: not  obj['comments'], users 
# ))
# print(active)
# print()
# print(inactive)


# ____________________________________________________________________________________

# names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira','Bob']

# res = list(map(
#     lambda x: f'Hello mr/mrs {x}', filter(
#         lambda x: len(x)>5, names 
#     )
# ))

# print(res)

# _______________________________________________________________________________________

# Функция Reduce () принимает функцию и последовательность и возвращает одно значение, 
# рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из 
# последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным 
# на шаге 1, и следующим значением в последовательности. 
# Этот процесс повторяется до тех пор, пока в последовательности 
# не закончатся элементы.

# более математическая функция раньше была встроеная теперь с 4 версии нужно импортировать 

# from functools import reduce
# ls = [1,2,3,4,5]
# sum_ = reduce(
#     lambda x,y: x+y, ls )
# res = reduce(
#     lambda x,y: x*y, ls )
# print(sum_,res)

# _____________________________________________________________________________________
# генератор пароля(самый совершенный генератор пароля)
# from itertools import repeat #
# # for x in repeat(lambda x: x,15): 
# #     print(x)
# from random import choices, shuffle #
# from string import ascii_letters, digits #
# from statistics import mean #выводит среднее значение 

# symbols = '!@#$%^&*()_-+=<>?/,. '

# q_pass = int(input('Введите кол-во паролей:'))
# result = {f(choices(ascii_letters, k =10), #asddfsaf
#             choices(digits, k = 5), #12323
#             choices(symbols, k = 2)) #@
#           for f in repeat(
#               lambda a,d,s: ''.join(set(a+d+s)), q_pass)

# }


# print(result)
# print(f'Quantity of passwords: {len(result)}')
# print()
# dlina = [len(x) for x in result]
# print(f'Average len: {mean(dlina)}')

