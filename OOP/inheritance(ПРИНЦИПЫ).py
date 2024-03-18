# Принципы ООП(механизмы):
# 1.Наследование 
# 2.Инкапсуляция 
# 3.Полиморфизм


# 4. Абстракция 
# 5. Композиция 
# 6. Агрегация 
#_________________________________________________________________________________

# Наследование
# Позволяет принимать родительские методы и атрибуты дочернему классу 

# Родительский класс 
# Дочерний класс 
# _________________________________________________________________________________

# class Animal: 
#     def print_info(self): 
#         print('I\'m an Animal!')

# class Lion(Animal): 
#     pass

# class Dog(Animal): 
#     pass

# lion = Lion()
# lion.print_info()

# print(dir(Lion))
# ____________________________________________________________________________________
# class Animal:
#     def say(self): 
#         print(f'This animals name is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'{self.name} eats:{self.meal}')

# class Lion(Animal): 
#     name = 'Lion'
#     golos = 'meat'
#     meal = 'meat'
#     griva = True
# class Dog(Animal): 
#     name = 'Alabel'
#     golos = 'bark'
#     meal = 'meat'
# class Koala(Animal): 
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalipt'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# # simba.info()
# print()
# julian.say()
# julian.eat()
# # julian.info()

# ________________________________________________________________________________________
# class Person: 
#     def info(self): 
#         print('I\'m person from Bishkek!')

# class Student(Person): 
#     def info(self): 
#         super().info() #он сначала срабатывает метод info у класса Person потом класса Student 
#         print('I study at Manas University')

# obj = Student()
# obj.info()

# ________________________________________________________________________________________
# class LapTop: 
#     def __init__(self, brand, model, price):
#         self.brand = brand 
#         self.model = model
#         self.price = price 

#     def get_info(self): 
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}
    

# class Acer(LapTop):
#     def __init__(self, model, price, year, videocard):
#         super().__init__('Acer', model, price) #в супер обычно передают первым self а вторым название класса(Acer)
#         self.year = year
#         self.videocard = videocard

#     def get_info(self):
#         repr = super().get_info() #возвращает словарь но нет 2 новых аттрибута(year,videocard)
#         repr['year']=self.year #передаем их в словарь
#         repr['vidoecard']=self.videocard
#         return repr
    
# class Apple(LapTop):
#     def __init__(self, model, price, display , year):
#         super().__init__('MacBook', model, price)
#         self.display = display
#         self.year = year 

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr 
    
# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# acer = Acer('swift',600,2019,'Nividia')
# print(acer.get_info())




