# найти квадрат куб и результат деления на 100 любых чисел 
# num = 5 
# {'num':5, }

# num1 = 5
# num2 = 75 
# num3 = 1123

# res1 = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1/100}
# res2 = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2/100}
# res3 = {'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3/100}

# print(res1,res2,res3, sep = '\n\n')
 
#  DRY - don't repeat youeself 


# num2 = 75 
# num3 = 1123

# res1 = {'num': num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1/100}
# res2 = {'num': num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2/100}
# res3 = {'num': num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3/100}

# def do_operations(num: 'int') -> None:
#     res = {'num': num, '2': num ** 2, '3': num ** 3, '100': num/100}
#     print(res)

# do_operations(5)
# do_operations(75)
# do_operations(1123)

#_________________________________________________________________________________________

# функция - это именованная чать программы, которая содержит
#  в себе определенный блок кода, и может 
# вызываться в длугих частях программы столько раз сколько угодно 

# def name_of_func(<a,b> параметры функции):
#     <body>код какая то логик
# , а 
#     <return> оператор который помогает сохранить результат 

# name_of_func(4,6 аргументы)

# параметры функции - данные в которых мы временно 
# сохраняем данные которые передаем при вызове в функции, они доступны только внутри функции 

# аргументы функции - данные которык мы передаем при вызове функции, 
# они попадает в параметры по очередно

# def isEven(num):
#     return True if num % 2 == 0 else False

# res = isEven(17)
# res1 = isEven(16)
# print(res,res1)

# def isEven(num: int) -> bool:
#     """Return True or Fslse after checking number for even"""
#     return True if num%2 == 0 else False 
#     # анатоции 

# _________________________________________________________________________

# def  sum_of_args(a: int, b: int, c: int=0 необязательные параметры всегда стоят в конце) -> int: 
#     """Returns sum of given arguments"""
#     try: 
#         return a+b+c
#     except TypeError:
#         raise Exception('Invalid values for arguments')
# print(sum_of_args(1,2,3))
# print(sum_of_args(2,9,23))
# # print(sum_of_args(1,5,None))

# ____________________________________________________________________________

# print(len('string'))

# from typing import Iterable

# def our_len(obj: Iterable) -> str: #итерируемый объект может включать в себя все что 
#     #угодно например строку список и тд
#     """ Возвращает длину итерируемого объекта"""
#     i = 0 
#     print(obj)
#     for _ in obj:
#         i +=1 
#     print(f'result: {i}')

# our_len([1,2,3,4,5])
# our_len('string Hello World my name is John Snow')
#  ___________________________________________________________________________________

# 'Hello wold! My name is Jonh, last name  is Snow. Nice to meet you!'
# 'you! meet to .......'

# def words_back(text: str) -> str:   
#     """Reversing text"""
#     spisok = text.split()
#     return ' '.join(spisok[::-1])
# print(words_back('Hello wold! My name is Jonh, last name  is Snow. Nice to meet you'))

# words_back()

# _______________________________________________________________________________________