    #########     Inheritance In Python     #########

'''В языке Python класс может быть создан либо как совершенно новый, либо как «производный» от существующего. Важно отметить, что производный класс наследует члены родительского (базового) класса, от которого он произошел, в дополнение к своим собственным членам.
Возможность наследовать члены из базового класса позволяет создавать производные классы, имеющие некоторые общие свойства, которые были определены для базового класса. Например, в базовом классе Polygon (Многоугольник) могут быть определены такие свойства, как ширина и высота, которые являются общими для всех многоугольников. Классы Rectangle (Прямоугольник) и Triangle (Треугольник) могут являться производными от класса Polygon, наследуя его свойства «ширина» и «высота», а также могут иметь свои собственные члены, определяющие уникальные свойства, присущие только им.
Чтобы объявить производный класс, нужно после его имени добавить
скобки, в которых указать имя родительского класса.'''

# class Polygon:
#   width = 0
#   height = 0
#   def set_values( self, width, height) :
#       Polygon.width = width
#       Polygon.height = height

# class Rectangle(Polygon):
#     def area(self):
#         return self.width * self.height

# class Triangle(Polygon) :
#     def area(self):
#         return(self.width * self.height) / 2

# rect = Rectangle()
# trey = Triangle()

# rect.set_values(4, 5)
# trey.set_values(4, 5)

# print('Rectangle Area:', rect.area())
# print('Triangle Area:', trey.area())


'''В языке Python класс равносилен понятию тип данных.
Что такое класс или тип? Проведем аналогию с реальным миром. Если мы возьмем конкретный стол, то это объект, но не класс. А вот общее представление о столах,их назначении – это класс. Ему принадлежат все реальные объекты столов, какими бы они ни были. Класс столов дает общую характеристику всем столам в мире, он их обобщает.
То же самое с целыми числами в Python. Тип int – это класс целых чисел. Числа 5,100134, -10 и т. д. – это конкретные объекты этого класса.
Например, мы можем создать свой класс, похожий на словарь:'''

# class Mydict(dict):
#     def get(self, key, default = 0):
#         return dict.get(self, key, default)

# a = dict(a=1, b=2)
# b = Mydict(a=1, b=2)

'''Класс Mydict ведёт себя точно так же, как и словарь, за исключением того, что
метод get по умолчанию возвращает не None, а 0.

Создание родительского класса в Python.
Создайте класс Person, с name в качестве свойства и двумя методами get_name(), is_student().
'''

# class Person(object):

#     # Constructor
#     def __init__(self, name):
#         self.name = name

#     # To get name
#     def get_name(self):
#         return self.name

#     # To check if this person is Student
#     def is_student(self):
#         return True

# person = Person("Влад")  # An Object of Person
# print(person.get_name(), person.is_student())

# # Вывод
# # Влад True

'''
Создание дочернего класса.
Если мы хотим создать класс, который наследует функциональность от другого класса, отправьте родительский класс в качестве параметра при создании дочернего класса. Смотрите следующий код.
'''

# class Student(Person):

#     # Here we return true
#     def is_student(self):
#         return False

'''
Теперь класс Student имеет те же свойства и методы, что и класс Person.

Используйте класс Student для создания объекта, а затем выполните методы get_name() и is_student().
'''

# student = Student("Айпери")  # An Object of Student
# print(student.get_name(), student.is_student())

# # Вывод
# # Айпери False

'''
Добавление ​​метода __init__().
Мы уже добавили конструктор внутри класса Person.

def __init__(self, name):
        self.name = name

Это означает, что во время создания объекта мы можем установить свойства класса.

Когда вы добавляете функцию __init__() в дочерний класс (в нашем случае это класс Student), дочерний класс больше не наследует родительский метод __init__().
Дочерний метод __init__() отменяет наследование родительского __init__().
Если мы хотим сохранить наследование родительского метода __init__(), добавьте вызов родительского метода __init__(). Смотрите следующий код.
'''

# class Student(Person):
#   def __init__(self, name):
#     Person.__init__(self, name)

'''
Одиночное наследование.
Когда дочерний класс наследует только от одного родительского класса, это называется одиночным наследованием. Мы видели пример выше.

Множественное наследование.
Когда дочерний класс наследуется от нескольких родительских классов, это называется множественным наследованием.
В отличие от Java и C ++, Python поддерживает множественное наследование. Мы указываем все родительские классы в виде списка через запятую в скобках.
'''

# class Base1(object):
#     def __init__(self):
#         self.str1 = "Eleven"
#         print("First Base Class")


# class Base2(object):
#     def __init__(self):
#         self.str2 = "Krunal"
#         print("Second Base Class")


# class Derived(Base1, Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived Class")

#     def print_data(self):
#         print(self.str1, self.str2)


# obj = Derived()
# obj.print_data()

# # Вывод
# # First Base Class
# # Second Base Class
# # Derived Class
# # Eleven Krunal

'''
Многоуровневое наследование
Многоуровневое наследование означает бабушка с дедушкой -> родители -> дети.
'''

# class GrandParents(object):

#     # Constructor
#     def __init__(self, name):
#         self.name = name

#     # To get name
#     def get_name(self):
#         return self.name


# # Inherited or SubClass
# class Parents(GrandParents):

#     # Constructor
#     def __init__(self, name, age):
#         GrandParents.__init__(self, name)
#         self.age = age

#     # To get name
#     def get_age(self):
#         return self.age


# # Inherited or SubClass
# class Children(Parents):

#     # Constructor
#     def __init__(self, name, age, address):
#         Parents.__init__(self, name, age)
#         self.address = address

#     # To get address
#     def get_address(self):
#         return self.address


# g = Children("Иван", 36, "Бишкек")
# print(g.get_name(), g.get_age(), g.get_address())

# # Вывод
# # Иван 36 Бишкек

'''
# Иерархическое наследование
Когда более одного класса является производным от одного базового класса, такое наследование известно как иерархическое наследование, где методы, которые являются общими на нижнем уровне, включаются в родительский класс.

Проблемы, в которых должна поддерживаться иерархия, могут быть эффективно решены с помощью этого наследования. Проще говоря, из одной базы создается более одного производного класса.

# Гибридное наследование
Гибридное наследование представляет собой комбинацию множественного наследования и многоуровневого наследования. Класс является производным от двух классов, как в множественном наследовании. Однако один из родительских классов не является базовым классом. Это производный класс. 

Гибридное наследование объединяет несколько форм наследования. Это смесь более чем одного типа наследования.
'''