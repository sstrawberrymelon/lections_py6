# 1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2,
# который наследуется от Class1, и определите в новом классе ещё 2 метода. 
# Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

# """

# class Class1:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price 

#     def get_info(self): 
#         return {'brand': self.brand, 'price': self.price}
     
#     def change_price(self): 
#         res1 = self.price * 2
#         print('Двойная цена:',res1)

    
    
# class Class2(Class1): 
#     def __init__(self, price,color):
#         super().__init__('Toyota', price)
#         self.color = color 

#     def get_info(self):
#         res = super().get_info()
#         res['color'] = self.color
#         return res 
    
#     def change_price(self, discount):
#         res2 = super().change_price() 
#         self.discount = discount
#         res3 = self.price - discount
#         print('Скидка:',res3)


        

        


# toyota = Class2(10000,'white')
# print(toyota.get_info())
# print(toyota.change_price(2000))






# """

# 2) Создайте класс A и определите в нём метод method1, который будет печатать строку
# "Основной функционал". Затем создайте второй класс B, который наследуется от класса A,
# и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". 
# Объявите экземпляр класса B и вызовите метод method1.

# """

# class A: 
#     def method1(self): 
#         print('Основной функционал')
    
# class B(A):
#     def method1(self): 
#         super().method1()
#         print('Дополнительный функционал')

# a = B()
# a.method1()




# """

# 3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
# append, который будет принимать строку и добавлять её в конец исходной
# pop, который удаляет из строки последний элемент и возвращает его.
# Пример
# # example = MyString('String')
# # example.append('hello')
# # print(example) -> 'Stringhello'
# # print(example.pop()) -> 'o'
# # print(example) -> 'Stringhell'
# """

# class MyString(str):
#     def __init__(self, string): 
#         super().__init__()
#         self.string = string

#     def append(self,str2): 
#         self.string += str2
        

#     def pop(self): 
#         last = self.string[-1]
#         self.string = self.string[:-1]
#         return last
    
#     def __str__(self) -> str:
#         return self.string


# example = MyString('String')
# example.append('hello')
# print(example.pop())
# print(example)



# """

# 4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. 
# Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего 
# ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

# """

# class MyDict(dict): 
#     def __init__(self, *args,**kwargs): 
#         super().__init__(*args,**kwargs)

#     def get(self,key, default='Are you kidding?'): 
#Параметры по умолчанию в Python позволяют упростить вызовы функций, 
#если не все аргументы передаются. Чтобы задать параметру значение по умолчанию, 
# нужно использовать оператор присваивания (=) в виде имя_параметра=значение
#         return super().get(key, default) 

# example = MyDict({'a': 'hello', 'b': 'world'})
# print(example.get('a'))
# print(example.get('c'))
        


# """

# 5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. 
# Создайте метод display(), который будет выводит данные об этом человеке.
# Создайте второй класс Student, который будет наследоваться от класса Person, 
# он должен принимать все атрибуты, которые были определены в родительском классе и
# добавьте еще один атрибут, который будет описывать направление студента.
# Создайте метод display_student(), который будет выводить данные об этом студенте.
# Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, 
# затем как о студенте.

# """

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self): 
#         return f'Name:{self.name}, Age:{self.age}'

# class Student(Person): 
#     def __init__(self, name, age, department):
#         super().__init__(name, age)
#         self.departement = department

#     def display_student(self): 
#         res = super().display()
#         return f'{res}\nDepartemnt:{self.departement}'

# example = Student('John Snow', 22,'Physics')
# print(example.display_student())

    

# """

# 6) Создайте класс ContactList, который должен наследоваться от 
# встроенного класса list. В нем должен быть реализован метод search_by_name, 
# который должен принимать имя и возвращать список всех совпадений. 
# Создайте экземпляр класса all_contacts и передайте список ваших контактов.

# """

# class ContactList(list): 
#     def __init__(self, ls = [] ):
#         self.ls = ls

#     def search_by_name(self, name): 
#         self.name = name
#         for i in self.ls:
#              if i == name: 
#                  return f'Совападенея:{i}'

# contacts = ContactList(['John', 'Raychel','Din','Sam'])
# print(contacts.search_by_name('Din'))          

# """

# 7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, 
# color, memory, battery. battery по умолчанию
# должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал 
# строку с названием и памятью смартфона.
# У данного класса также должен быть метод charge, который увеличивает значение
# батареи на указанную величину.
# Создайте два дочерних класса от Smartphone - Iphone и Samsung.
# У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает 
# строку с сообщением и от какого телефона оно было выслано.
# А у Samsung должен быть дополнительный аттрибут android и метод show_time, 
# который показывает текущее время.
# Создайте объекты от данных классов и примените все методы.

# """
# from datetime import datetime
# class Smartphone: 
#     battery = 0
#     def __init__(self, name, color, memory) -> None:
#         self.name = name 
#         self.color = color
#         self.memory = memory
        
    
#     def str(self): 
#         return f'Name:{self.name}\nMemory{self.memory}, {self.battery}'
    
#     def charge(self, level):
#         self.battery += level
#         return self.battery
    
# class Iphone(Smartphone): 
#     def __init__(self, name, color, memory) -> None:
#         super().__init__(name, color, memory)
#         self.ios = 'ios'

#     def send_imessage(self, message, phone):
#         self.message = message
#         self.phone = phone 
#         return f'Message:{self.message}from{self.phone}'
# class Samsung(Smartphone):
#     def __init__(self, name, color, memory) -> None:
#         super().__init__(name, color, memory)
#         self.android = 'android'
        
#     def show_time(self):
        
#         return f'Time:{datetime.now()}'
    

# example = Samsung('Ultra S5','black', '128GB')
# example1 = Iphone('15 Pro Max','white','256 GB')
# print(example.show_time())
# print(example1.send_imessage('Hello World','Iphone SE'))
# print(example.charge(10))
# for i in [example, example1]:
#     print(i.str())


    

    
        
 

# """

# 8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют 
# два аттрибута - name - название и formula - полное произношение заклинания. 
# У класса есть два метода: get_description() - дает полное описание заклинания 
# и execute() - совершает заклинание.
# Переопределите у класса метод str, чтобы он выдавал вам название, 
# формулу и описание вместе, к примеру:
# Открытие замков: Alohomora
# позволяет магу попасть в любую комнату,
# способно открыть любую закрытую замочную скважину.
# Наследуя от класса Spell создайте три заклинания,переопределяя 
# в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

# class Spell:

#     def get_description(self,name): 
#         self.name = name  
#         return self.name

#     def execute(self,formula ):
#         print('hiii')
#         self.formula = formula
#         return self.formula
     
#     def str(self): 
#         return f'Открытие замков:{self.name}\n{self.formula}'

# class Ahalai(Spell): 
#     pass
    
# class Mahalai(Spell): 
#     pass
# class Bahalai(Spell):
#     pass
  

# for1 = Bahalai()
# print(for1.get_description('Bahalai'))
# print(for1.execute('fly'))



# 9. Напишите класс CustomError который наследуется от встроенного класса 
# исключений Exception. Переопределите init таким образом
# чтобы через экземпляр класса можно было передавать сообщение и
# создавать новые виды исключений.
# Создайте исключение от этого класса с сообщением:
# "ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ" 
# Напишите функцию проверяющую строки на регистр и если строка не написана
# в верхнем регистре выбросите исключение созданное классом CustomError:
# Traceback (most recent call last):
#   File "inheritance.py", line 121, in <module>
#     check_letters(a)
#   File "inheritance.py", line 117, in check_letters
#     raise capitals_error
# main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

# """
# class CustomerError(Exception): 
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)

#     def check(self, message):
#         self.message = message 
#         for i in self.message: 
#             if i.islower(): 
#                 raise CustomerError(self.args)
            
# str = CustomerError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
# str.check('HELLo')


# """

# 10. Создайте класс Character с помощью которого можно создавать героев для игры.
# Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная 
# power_list, в которой хранится словарь:
# power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }
# Класс должен иметь методы:
# give_weapon - выбирает случайное оружие из списка
# give_role - выбирает случайную роль из списка, к примеру:
# ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
# give_powers, передавая силу и значение можно менять power_list для определенного героя,
# к примеру:
# char1.give_powers('ловкость', 5)
# увеличит ловкость вашего героя.
# Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,
# дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра 
# класса,наследуя init от Character. Создайте несколько героев от этих классов и
# вызовите их методы и методы родительского класса Character.
# import random 
# class Character:
#     weapon_list = ['Меч','Нож','Лук','Кастет','Пистолет','Бита']
#     role_list = ["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#     power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

    
#     def __init__(self,name) -> None:
#         self.name = name
        
#     def give_weapon(self): 
#         rand = random.choice(self.weapon_list)
#         return f'Ваше оружие:{rand}'
        
#     def give_role(self): 
#         rand = random.choice(self.role_list)
#         return f'Ваше роль:{rand}'

#     def give_powers(self,key, velue): 
#         if key in self.power_list:
#             self.power_list[key]+=velue
#             return self.power_list
        

# class Elf(Character): 
#     def __init__(self, name, disease) -> None:
#         super().__init__(name)
#         self.disease = disease

# class Orc(Character): 
#     def __init__(self, name, advantage) -> None:
#         super().__init__(name)
#         self.advantage = advantage 

# class DragonBorn(Character): 
#     def __init__(self, name, disadvantage) -> None:
#         super().__init__(name)
#         self.disadvantage = disadvantage
#     def __str__(self) -> str:
#         return self.disadvantage

# a = DragonBorn('john','Cлишком большой')
# a.give_powers('мудрость',10)
# a.give_powers('харизма',3)
# print(a.give_powers('интеллект',9))
# print(a.give_role())
# print(a.give_weapon())
# print(a)








        