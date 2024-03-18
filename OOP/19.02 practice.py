# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, 
# и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный 
# аттрибут - радиус. Также класс должен иметь метод расчета площади круга. 
# Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
# """
# class Circle: 
#     Pi = 3.14
#     color = 'blue'
    
#     def __init__(self, radius) -> None:
#         self.radius = radius 

#     def s(self):  
#         self.res = 2 * self.Pi * self.radius
        

#     def info(self): 
#         print(f'Радиус = {self.radius} тогда площадь его: {self.res}!')     


# r1 =Circle(2)
# r2 = Circle(3)
# r3 = Circle(6)

# r1.s()
# r2.s()
# r3.s()

# r1.info()
# r2.info()
# r3.info()


# """
# 2) Создайте класс для песен Song. Каждая песня имеет название, 
# автора и год выпуска. Добавьте три метода show_author, show_title, 
# show_year, выводящие утверждения о каждом атрибуте экземпляра класса 
# Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса 
# с вашей любимой песней и примените все методы.
# """
# class Song: 
#     def __init__(self, title, author, year) -> None:
#         self.title = title 
#         self.author = author 
#         self.year = year 

#     def show_title(self): 
        
#         print(f'Название песни: {self.title}')

#     def show_author(self):
        
#         print(f'Автор песни: {self.author}')

#     def show_year(self): 
        
#         print(f'"Эта песня вышла в {self.year} году"')

# v = Song('Slow Dancing','V','2023')
# iu = Song('Love wins All','IU','2024')


# v.show_title()
# v.show_author()
# v.show_year()

# iu.show_title()
# iu.show_author()
# iu.show_year()



# """
# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название 
# компании, стоимость посадки, стоимость за каждый пройденный километр. Также 
# добавьте к классу метод расчитывающий стоимость поездки. Создайте 
# три экземпляра класса Taxi для трех разных компаний Namba, Yandex и 
# Jorgo и расчитайте стоимость поездки на каждом из них.
# """
# class Taxi: 
#     dis = 8

#     def __init__(self, name, price, km ) -> None:
#         self.name = name 
#         self.price = price
#         self.km = km 

#     def count(self): 
#         self.res = self.dis * self.km + self.price
#         print(f'Стоимость поездки {self.name} Taxi составляет {self.res}!')

# namba = Taxi('Namba',110,12)
# yandex = Taxi('Yandex',100, 13)
# jorgo = Taxi('Jorgo', 99, 11)

# namba.count()
# yandex.count()
# jorgo.count()


# """
# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии 
# и номер телефона. Также создайте метод get_info, который выводит информацию 
# о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
# """
# class Phone:

#     def __init__(self, name, surname, number) -> None:
#         self.name = name 
#         self.surname = surname 
#         self.number = number 

#     def get_info(self): 
#         res = self.name + ' ' + self.surname
#         print(f"Контакт:{res} , телефон:{self.number}")

# p1 = Phone('Ivan','Petrov',996700000000)

# p1.get_info()

        



# """
# 5) Напишите класс Salary для расчета налогов на заработную плату. 
# У класса должна быть обязательная переменная класса - процент 
# налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты 
# и стаж работы в качестве атрибутов. Также у класса должен быть метод 
# расчитывающий сумму налога заплаченного за весь стаж работы. Создайте 
# экземпляр класса и посчитайте сумму вашего налога.
# """

# class Salary: 
#     per = 8
    
#     def __init__(self, sal, time ) -> None:
#         self.sal = sal 
#         self.time = time 

#     def count(self): 
#         res = (self.time * 12) * (self.sal * 0.08) 
#         print(f'Сумма вашего налога за весь период работы {res} сом! ')

# ivan = Salary(30000, 2)         
# ivan.count()


# __________________________________________________________________________________________
# Создайте класс Soda принимающий 1 аргумент при инициализации 
# (отвечающий за добавку к выбираемому лимонаду).
# В этом классе реализуйте метод show_my_drink(), выводящий на печать 
# «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится 
# следующая фраза: «Обычная газировка».


# class Soda: 
#     def __init__(self, dobavka=None) -> None:
#         self.dobavka = dobavka

#     def show_my_drink(self): 
#         if self.dobavka: 
#             print(f'Газировка {self.dobavka}')
#         else: 
#             print(f'Обычная газировка!')
# straw = Soda()
# straw.show_my_drink()


# __________________________________________________________________________________________
# Создайте класс Student. При создании его экземпляра, мы должны записать 
# имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
#  1 переменная объекта books = [ ]
#  2 переменная объекта “knowledge” со значением по умолчанию 0
#  3 метод read_book, который принимает название книги, добавляет книгу в books, 
# добавляет 100 баллов в knowledge
#  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
#  5 Создайте экземпляры, вызовите методы.

# class Student: 
#      books = [ ]
#      knowledge = 0 
#      def __init__(self, name, surname) -> None:
#         self.name = name
#         self.surname = surname 
#         print(f'имя:{self.name} \nфамилия:{self.surname}')

#      def read_book(self,book): 
#          self.book = book 
#          self.books.append(book)
#          self.knowledge += 100 
#          print(f'Название книги: {self.book}')


#      def do_homework(self): 
#          self.knowledge += 10 

# md = Student('Иван','Иванович')
# md.read_book('Мертвые души')
# md.do_homework()


# Создайте класс имеющий атрибут "дата рождения" и автоматически 
# просчитываемый возраст по входящей дате рождения. Используйте м<
# одуль time/datetime

# class Birth: 


# Задание 1: Класс "Комната" и "Дом"
# Цель: Практика в создании взаимодействующих объектов и управлении ими.

# Задача: Создайте класс Комната с атрибутами название, ширина и длина. 
# Добавьте метод, который вычисляет площадь комнаты. Затем создайте класс Дом, 
# который содержит список комнат. В классе Дом должны быть методы для добавления 
# комнаты и вычисления общей площади дома.

    
# class Room: 
#     def __init__(self, name, width, length) -> None:
#         self.name = name 
#         self.width = width 
#         self.length = length 

#     def square(self): 
#         s = self.width * self.length

    
# class House: 

#     def __init__(self, ls: list) -> None:
#         self.ls = []
#     obj = Room()

        


# Задание 3: Класс "Библиотека" и "Книга"
# Цель: Работа с коллекциями объектов и их методами.

# Задача: Расширьте класс Книга из предыдущего задания, 
# добавив атрибут количество. Создайте класс Библиотека, 
# который будет содержать список книг. В классе Библиотека реализуйте 
# методы для добавления книги (с учетом уже существующих тайтлов), 
# удаления книги по названию, и поиска книг по автору.

    

# Задача: Создание системы учета сотрудников для компании

# Цель: Разработать классы для управления информацией о сотрудниках в компании, 
# включая их отделы, должности и личные данные.

# Описание:

# Класс Employee:



class Employee: 
    def __init__(self, name, employee_id, position, department) -> None:
        self.name = name
        self.employee_id = employee_id
        self.position = position 
        self.department = department 

    def promote(self,new_position):
        self.new_position = new_position
    def transfer(self, new_department):
        self.new_department = new_department

    def __str__(self) -> str:
        return f'Employee:{self.name}\nID:{self.employee_id}\nPosition:{self.position} \nDepartment:{self.department}'
        
class Department: 
    def __init__(self,name,department_id, employees=[]) -> None:
        self.employees = employees
        self.name = name 
        self.department_id = department_id

    def add_employee(self, employee):
        
        self.employees.append(employee)
        
    def remove_employee(self, employee):
        self.employees.remove(employee)

    def get_employees(self): 
        print(f'Список сотрудников отдела:{self.employees}')

    def __str__(self) -> str:
        print(f'Отдел:{self.name}\n Сторудники:{self.employees}')
    
class Company: 
    def __init__(self, name, departments=[], emplpoyees=[] ) -> None:
        self.name = name 
        self.departmnets = departments
        self.employees = emplpoyees
    def add_department(self, department):
        self.departmnets.append(department)

    def add_employee(self, employee, dep_id): 
        for i in self.departmnets: 
            if dep_id == i.department_id: 
                self.employees.append(employee)
    def find_employee(self, employee_id):
        for i in self.employees: 
            if employee_id == i.employee_id: 
                print(i)

    def find_departemnt(self,department_id):
        for i in self.departmnets: 
            if department_id == i.department_id: 
                print(i)

    def transfer(self, employee_id, department_id): 
        for i in self.employees: 
            if employee_id == i.employee_id: 
                for x in self.departments: 
                    if department_id == x.department_id:
                        i.transfer(x)

codify = Company('Codify')
empl1 = Employee('Tata', 1,'boss','IT')
empl2 = Employee('Cooky', 2,'boss','Marketing')
empl3 = Employee('Chimmy', 3,'boss','PO')
empl4 = Employee('RJ', 4,'boss','Production')
empl5 = Employee('Shooky', 5,'boss','Entertainment')
empl6 = Employee('Mang', 6,'boss','Logistics')
empl7 = Employee('Koya', 7,'boss','Sales')

empl1.promote('director')
print(empl1)

                    

        

                    




            

                
                

    
                        

# Атрибуты: name (имя сотрудника), employee_id (ID сотрудника), position (должность), 
# department (отдел).
# Методы:
# Конструктор для инициализации атрибутов.
# promote(new_position) - повышение сотрудника на новую должность.
# transfer(new_department) - перевод сотрудника в другой отдел.
# __str__() - возвращает информацию о сотруднике.

# Класс Department:

# Атрибуты: name (название отдела), department_id (ID отдела), employees 
# (список сотрудников в отделе).
# Методы:
# Конструктор для инициализации атрибутов.
# add_employee(employee) - добавляет сотрудника в отдел.
# remove_employee(employee_id) - удаляет сотрудника из отдела.
# get_employees() - возвращает список сотрудников отдела.
# __str__() - возвращает информацию об отделе и его сотрудниках.

# Класс Company:

# Атрибуты: name (название компании), departments (список отделов в компании), employees 
# (список всех сотрудников).
# Методы:
# Конструктор для инициализации атрибутов.
# add_department(department) - добавляет новый отдел в компанию.
# add_employee(employee, department_id) - регистрирует нового сотрудника и добавляет 
# его в указанный отдел.
# find_employee(employee_id) - ищет сотрудника по ID.
# find_department(department_id) - ищет отдел по ID.
# transfer_employee(employee_id, new_department_id) - переводит сотрудника в другой отдел.
# Задание:
# Реализуйте вышеуказанные классы с соответствующими атрибутами и методами. 
# Создайте взаимодействие между классами так, чтобы можно было управлять информацией 
# о сотрудниках, их должностях и отделах. Обеспечьте возможность добавления новых 
# сотрудников и отделов, а также перевода сотрудников между отделами и их повышения в должности.

