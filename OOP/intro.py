# ООП - объектно-ориентированное программирование 
# Класс - эьл описание того, как должен выглядеть объект, то есть в классе мы описываем
# какими свойствами(данными) и поведением (функциями) должен обладать объект 

# Объект - это некая сущность, которую мы создаем от класса, у объекта есть собственное 
# состояние свойств(данные)
# 

# Аттрибуты - обычные переменные внутри класса 
# Методы - функция внутри класса 

# ____________________________________________________________________________________

# class Human:
#     age = 0

#     def __init__(self, first_name,last_name, job, citizenship): 
#         self.name = first_name+' '+ last_name
#         self.job = job
#         self.citizen = citizenship

#     def show_info(self):
#         return f'Name:{self.name}, Age:{self.age}, Job: {self.job}, Citizen:{self.citizen}'

# john = Human('John', 'Snow', 'King of North', 'Northerner')
# anvar = Human('Anvar','Lanister', 'Programmer','Kyrgyz Republic')


# print(john)
# print(type(john))
# print(dir(john))
# print(john.show_info())
# print(anvar.show_info())
# john.age = 24 
# john.job = 'King of Westeros'
# print(john.show_info())
# _________________________________________________________________________________

# class Dog:
#     # аттрибуты класса 
#     age = 0 
#     ushi = True

#     def __init__(self, name: str, color: str) -> None: 
#         """Именно здесть создаются аттрибуты объекта"""
#         # self - ссылка на объект который создается 
#         self.name = name 
#         self.color = color 

#     def bark(self):
#         print(f'{self.name} лает!')

#     def show_info(self): 
#         print(f'Name:{self.name}, Age: {self.age}, color: {self.color}, ushi:{self.ushi}')

# rex = Dog('Rex','black')
# pluto = Dog(name='Pluto', color='brown')
# aktosh = Dog('Aktosh','gray')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2

# pluto.age = 7
# aktosh.age = 1
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()
# aktosh.bark()

# __________________________________________________________________________________________

# class Human: 
#     def __init__(self,name) -> None:
#         self.name = name 
#         self.golod = 100
    
#     def walk(self): 
#         print(f'{self.name} walking around!')
#         self.golod += 30

#     def work(self): 
#         print(f'{self.name} rabotu rabotaet!')
#         self.golod += 50 

#     def eat(self, meal, finish = True):
#         print(f'{self.name} покушала {meal}!')
#         self.golod -= 60 if finish else 30 

#     def info(self): 
#         print(f'{self.name} --> {self.golod}')

# obj = Human('Raychel')
# obj.info() 
# obj.eat('Kruasan')
# obj.eat('Sandwitch', finish=False)
# obj.walk()
# obj.work()
# obj.info() 
# obj.eat('Burger')
# obj.eat('Fried Potato',finish=False)
# obj.info() 


