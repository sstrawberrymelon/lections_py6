# 1)Автомобиль: создайте класс с именем Car. Метод __init__ () 
# класса Car должен содержать три атрибута: brand, year и color. 
# Создайте метод get_auto(), который выводит информацию об автомобиле, 
# и метод get_year, который выводит возраст авто .

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять 
# по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . 
# Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. 
# Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# class Car: 
#     horsepower = 85 
#     def __init__(self, brand, year, color ) -> None:
#         self.brand = brand 
#         self.year = year
#         self.color = color 

#     def get_auto(self): 
#         print(f'Автомобиль бренда {self.brand} {self.color} цвета!')

#     def get_year(self): 
#         print(f'{self.year} года!')

#     def add_horsepower(self): 
        
#         if self.brand == 'Mers' or self.brand == 'Bmw' or self.brand == 'Porshe': 
#             self.horsepower += 40 
#             print(f'Horsepower: {self.horsepower}')
#         else:
#             self.horsepower += 20 
#             print(f'Horsepower: {self.horsepower}')



# bmw = Car('Bmw',1999, 'yellow')
# print(bmw.brand)
# print(bmw.year)
# print(bmw.color)


# bmw.get_auto()
# bmw.add_horsepower()
# print(bmw.horsepower)

# tesla = Car('TESLA', 2024, 'pink')
# byd = Car('BYD', 2024, 'white')

# tesla.get_auto()
# byd.get_auto()



# 2)Студенты: создайте класс с именем Student. Создайте атрибуты name, 
# age, course. Напишите метод get_student(), который выводит сводку с 
# информацией о студенте . Создайте еще один метод get_birth_year() 
# для вывода информации о годе рождения студента.
# Создайте несколько экземпляров, представляющих разных студентов. 
# Вызовите оба метода для каждого студента.

class Student: 
    def __init__(self, name, age, course) -> None:
        self.name = name
        self.age = age 
        self.course = course
    
    def get_student(self):
        print(f'Student name: {self.name}\nAge: {self.age}\nCourse: {self.course}\n')
        
    def get_birth_year(self, day, month, year): 
        self.day = day 
        self.month = month 
        self.year = year 
        print(f'Date of birth: {self.day} {self.month} {self.year}')

        
# anna = Student('Anna', 14, 2)
# anna.get_student()
# anna.get_birth_year(12,'Jan', 2007)
