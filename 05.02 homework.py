# 1) Создайте функцию, которая генерирует рандомное (случайно сгенерированное) 
# число и выводит на окно терминала через команду print(). Далее создайте декоратор, 
# который журналирует это событие. То есть функция декоратор должна писать 
# в dict() предложение: «Функция …………… была запущена успешно», а ключом будет 
# уникальный идентификатор (id).   (15 баллов)

# import random 

# def function(func):
#     def wrapper(**kwargs): 
#         print(f'Функция {func.__name__} была запущена!')
#         print(func())
#     return wrapper




# @function 
# def Generator(): 
#     """Генерирует рандомные числа"""
#     res = random.randint(1,100)
#     print(f'Случайное число {res}')

# Generator()


# _______________________________________________________________________________________

# 2) Напишите функцию, которая принимает фразу, и возвращает его сокращенную форму.
# Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. 
# For your interest -- FYI и т.п. (10 баллов)

# def ShortName(phrase):
#     """Программа превращает фразу в абривиатуру
#     Args: 
#         принимает фразу 
#     Result: 
#         возвращает абривиатуру"""
    
#     words = phrase.split()
#     name = []
#     for i in words: 
#         if len(i) > 2: 
#             name.append(i[0].upper())
#         else: 
#             name.append(i)
#     return "".join(name)

    

# print(ShortName(input('Введите фразу:')))
#______________________________________________________________________________________________

# 3) '''Напишите декоратор, который проверяет, что функция вызывается с 
# определенными типами аргументов.''' (15 баллов)

# def function(func): 
#     def wrapper(*args,**kwargs):
#         s = True
#         for i in args: 
#             if type(i) != type(func(*args)[0]):
#                 s = False
#         print(s)
#     return wrapper

        
# @function
# def arg(a,b,c): 
#     return a,b,c

# arg(2,4,'dfsf') 
    
        

# ________________________________________________________________________________________

# 4) '''Создайте декоратор, который автоматически преобразует результат 
# функции в другой тип данных,''' (15 баллов)

# def function(func): 
#     def wrapper(*args,**kwargs):
#         print(type(func(*args,**kwargs)))
#         a = str(func(*args,**kwargs))
#         return type(a)
#     return wrapper

        
# @function
# def arg(a,b,c): 
#     return a + b + c 

# print(arg(1,1,1)) 
# _______________________________________________________________________________________

# 5) '''Реализуйте декоратор, который ограничивает максимальное количество 
# вызовов функции.''' (20 баллов)


# def decorator(func): 
#     global counter
#     counter = 0 

#     def wrapper(*args,**kwargs):
#         global counter
#         if counter < 3:
#             counter+=1
#             func()
#         else:
#             print('Функцию больше 3 раз вызывать нельзя!')
        
#     return wrapper

        

# @decorator
# def myfunc(): 
#     print('Функция myfunc была вызвана!')
# myfunc()
# myfunc()
# myfunc()
# myfunc()
# ______________________________________________________________________________________

# 6) '''Напишите декоратор, который автоматически логирует исключения, 
# возникающие внутри функции.''' (15 баллов)
# def decorator(func): 
#     def wrapper(*args,**kwargs):
#         try: 
#             return func(*args,**kwargs)
#         except: 
#             raise TypeError('Wrong!')
#     return wrapper 
# @decorator
# def myfunc(a,b):
#     return int(a)+int(b)
# a = input('Введите число:')
# b = input('Введите число:')
# print(myfunc(a, b))


# _____________________________________________________________________________________________ 

# 7) '''Напишите декоратор, который ограничивает доступ к функции только 
# определенным пользователям или ролям.''' (15 баллов) 

# def decorator(func): 
#     def wrapper(*args,**kwargs): 
#         ls = ['John', 'Sam','Jane']
#         s = True 
#         for i in args:
#             if i in ls:
#                 func(*args,**kwargs)
#             else:
#                 print('нет доступа!')
#     return wrapper
# @decorator
# def login(name): 
#     print(f'my name is {name}')

# login(input('Введите имя:'))



