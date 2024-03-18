# 1. Создайте класс BankAccount, в конструкторе которого определена переменная
# экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
# который будет отнимать сумму от баланса и возвращать текущий баланс. Также
# добавьте метод deposit, который также имеет параметр amount и соответсвенно
# добавляет сумму к балансу, возвращает баланс.
# """
# class BankAccount: 
#     balance = 0
#     def withdraw (self, amount): 
#         self.amonut = amount 
#         self.balance -= self.amonut
#         print(f'Текущий балас: {self.balance}')


#     def deposit(self, amount): 
#         self.amonut = amount
#         self.balance += amount
#         print(f'Текущий балас: {self.balance}')

# j = BankAccount()
# j.deposit(1200)
# j.withdraw(300)



# """
# 2. Вам дан такой код:
# class Nobel:   
#     def __init__(self, category , year, winner ): 
#         self.category = category
#         self.year = year 
#         self.winner = winner 

#     def get_year(self ): 
#         res = 2024 - self.year 
#         return f'Выиграл {res} лет назад!'
    
# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())



   

# который выводит в терминал такие значения:

# Литература 1971 Пабло Неруда
# выиграл 50 лет назад

# Литература 1994 Кэндзабуро Оэ
# выиграл 27 лет назад

# Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код 
# вывел указанные значения в терминале. Даты внутри класса не хардкодить.
# """

# 3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. 
# У класса должен быть метод validate для валидации пароля:
# - пароль должен быть минимум 8 символов, но меньше 15
# - пароль должен содержать цифры
# - пароль должен содержать буквы
# - пароль должен содержать хотя бы один из символов:
#     '@', '#', '&', '$', '%', '!', '~', '*'

# если одно из условий не выполнено, выводите кастомное исключение, 
# если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

# Также переопределите метод str, чтобы при попытке распечатать
# сам пароль, вам выдавалась строка из звездочек,
# к примеру пароль - 'joe@123456'
# в терминале выйдет - ******
# """

# from string import ascii_letters,digits
# class Password: 
#     symbols = '!@#$%^&*()_-+=<>?/,. '
#     def __init__(self, password) -> None:
#         self.password = password

#     def validate(self): 
#         print(type(digits))
#         if len(self.password) in range(8, 16) and [i for i in self.password if i in self.symbols] and [i for i in self.password if i in ascii_letters] and [i for i in self.password if i in digits]:
#             print('Ваш пароль успешен') 
#         else: 
#             raise ValueError

# w = Password('asdasf')
# v = Password('@aliya1221')

# v.validate()





            



# """
# 4. Создайте класс Math, экземпляром которого должно быть число.
# У классa Math должно быть 3 метода:
# - get_factorial - выводит факториал числа
# - get_sum - выводит сумму цифр числа
# - get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр 
# класса и примените к нему все методы. 

# class Math:
#     def __init__(self, digit ) -> None:
#         self.digit = digit

#     def get_factorial(self): 
#         f = 1
#         for i in range(1, self.digit+1):
#             f *= i
#         print('Факториал:', f)

#     def get_sum(self): 
#         res = 0
#         for i in str(self.digit):
#             res += int(i)
#         print('Сумма:',res)

#     def get_mul_table(self): 
#         for i in range(1,11): 
#             print(f'{self.digit} x {i} = {self.digit * i}')
            
# w = Math(22)
# w.get_factorial()
# w.get_mul_table()
# w.get_sum()

                                                                                                                                                                                                                                                                             


        



# 5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в 
# кино, сделать домашку, выгулять собаку и.т.д)

# У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) 
# с ключом в виде числа, 
# приоритет который вы даете вашей задаче -
# к примеру {3: 'сходить в кино'}
# приоритет сходить в кино у вас не самый высокий.

# У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
# по приоритету:
# [(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

# class ToDo: 
#     a = 'сходить в кино'
#     b = 'сделать домашку'
#     d = 'выгулять собаку'
#     dict_ = {}

#     def give_priority(self): 
#         self.dict_['1'] = self.b
#         self.dict_['2'] = self.d
#         self.dict_['3'] = self.a
        

#     def list_of_tasks(self): 
#         print(self.dict_)

    
# w = ToDo()
# w.give_priority()
# w.list_of_tasks()








