#############       Миксины       #############

'''
Язык программирования Python реализует как стандартное одиночное наследование:
'''

# class Mammal:
#   className = 'Mammal'

# class Dog(Mammal):
#   species = 'Canis lupus'

# dog = Dog()
# print(dog.className) 

# # Mammal


'''
так и множественное:
Мно́жественное насле́дование — свойство, поддерживаемое частью объектно-ориентированных языков программирования, когда класс может иметь более одного суперкласса (непосредственного класса-родителя), интерфейсы поддерживают множественное наследование во многих языках программирования. Эта концепция является расширением «простого (или одиночного) наследования» (англ. single inheritance), при котором класс может наследоваться только от одного суперкласса.
'''

# class Horse():
#   isHorse = True

# class Donkey():
#   isDonkey = True

# class Mule(Horse, Donkey):
#     pass


# mule = Mule()
# print(mule.isHorse) 
# print(mule.isDonkey) 

# # True
# # True

'''
Используя множественное наследования можно создавать классы-миксины (примеси), представляющие собой определенную особенность поведения. Такой микси можно "примешать" к любому классу.

Миксины - это те же классы, они ничем не отличаются от обычных. Единственное,что их объединяет - это то, что они не предназначены для создания экземпляров напрямую. Их цель - создать переиспользуемый инструмент, который будет использоваться субклассами для расширения их функционала.
Пример:
'''

# class CraneMixin:
#     def lift(self, thing):
#         print( '{} is lifted'.format(thing))


# class Transport:
#     def go(self):
#         print('whoom')
    
#     def carry_goods(self):
#         print('carrying goods')
    

# class Car(Transport):
#     def carry_passengers(self):
#         print ('carrying passengers')

    
# class TruckWithCrane(Transport, CraneMixin):
#     def carry_things(self):
#         print ('Carrying things')


# class MotorBoatWithCrane(Transport, CraneMixin):
#     def dock(self):
#         print ('stopped and docked')

'''
Создан миксин CraneMixin (можно назвать без применения слова Mixin - это необязательно), который самостоятельно ценности не несет, но расширяет функциональные возможности субклассов TruckWithCrane, MotorBoatWithCrane.
'''

# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def eat_grass(self):
#         print('eating green grass')


# class MilkOutMixin:
#     def milking(self):
#         print("If you doit' {}, you can have planty of milk".format(self.name))


# class Cow(Animal, MilkOutMixin):
#     pass

# class Goat(Animal, MilkOutMixin):
#     pass


# penny = Cow('penny')
# denny = Goat('denny')

# penny.milking()
# denny.milking()

# # If you doit' penny, you can have planty of milk
# # If you doit' denny, you can have planty of milk