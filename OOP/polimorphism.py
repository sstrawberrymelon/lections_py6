# Функция полиморфизм -> len():__len__
# print(len('Makers'))
# print(len([1,2,3,4,5]))
# print(len({1:2,3:4,5:3}))

# + (__add__) - метод работает у всех по разному 
# print(5+5)
# print('hello'+'world')
# print([1,2,3]+[4,5,6])

# Полиморфизм - способность функции(метода) использоваться для разных типов(классов)
# Широко распространенное определение: один интерфейс - много реализаций
# list.pop
# set.pop
# dict.pop

# class Cat: 
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age 

#     def info(self): 
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self): 
# class Cat: 
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age 

#     def info(self): 
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self): 
#         print('meow, meow!')

# class Dog: 
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age 

#     def info(self): 
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self): 
#         print('bark, bark!')
   
# cat = Cat('Kesha',5)
# dog = Dog('Pluto',3.)

# for obj in (Cat,Dog):
#     obj.info()
#     obj.make_sound() 
#         print('meow, meow!')

# class Dog: 
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age 

#     def info(self): 
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self): 
#         print('bark, bark!')
   
# cat = Cat('Kesha',5)
# dog = Dog('Pluto',3.)

# for obj in (Cat,Dog):
#     obj.info()
#     obj.make_sound() 


# _________________________________________________________________________________
# Абстракция (метод) - повышение гибкости кода, сочетание наследования, описание того как 
# должно наследоваться 

# from abc import ABC, abstractmethod #abstract base class 

# class Shape: 
#     def __init__(self,name) -> None:
#         self.name = name
    
#     @abstractmethod
#     def area(self): 
#         pass

#     @abstractmethod
#     def fact(self): 
#         pass 

# class Square(Shape): 
#     def __init__(self,lenght) -> None:
#         super().__init__('Квадрат')
#         self.length = lenght

#     def area(self):
#         return self.length ** 2  

#     def fact(self):
#         return 'У квадрата все стороны равны и углы равны 90 градусам' 
    
# class Circle(Shape): 
#     def __init__(self, radius) -> None:
#         super().__init__('Окружнсоть')
#         self.radius = radius 

#     def area(self):
#         from math import pi
#         return pi * self.radius ** 2
    
#     def fact(self): 
#         return 'Окружность это множество точек плоскости, расстояние которых до данной точки(центра окружности)одинаково'

# a = Square(5)
# b = Circle(2)

# print(a.area())
# print(a.fact())

# print(b.area())
# print(b.fact())


   