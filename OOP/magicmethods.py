# magic methods - магические методы
# dunder methods (double underscore) -> init
# служебные методы

# Магия(фишка) заключается в том, что эти методы запускаются без прямого обращения к ним, определенные методы могут отвечать за определенные операторы.

# Магические методы сравнения
# eq(self, other) -> 5 == 8
#  5eq(8)
# ne -> !=
# lt -> <
# gt -> >
# le -> <=
# ge -> >=

print('15' > 'ABC') # ASCII

class Word(str):
    def new(cls, obj): # cls - отсылка к самому классу Word 
        obj = obj.replace(' ', '')
        return super().new(cls, obj)
    
    def init(self, obj) -> None:
        super().init()
        self.obj = obj
    def gt(self, other): # obj - gt - obj2
        print('gt worked')
        print(self, '----', other)
        if len(self) > len(other):
            return self
        elif len(self) < len(other):
            return other
        else:
            return 'eq'
        
    def __lt__(self, other) -> bool:
        return len(self) < len(other)
    
    def __eq__(self,other) -> bool:
        return len(self) == len(other)
    


obj = Word('      Hello World   ')
obj2 = Word('Cod i fy')

print(obj > obj2)
print(obj < obj2)
print(obj == obj2)

_____________________________________________________________________
# + - / * // % ** dunder method math opertations 

# + -> __add__
# - -> __sub__
# * -> __mul__
# // -> __floordiv__
# / -> __div__(py2) -> __truediv__(py3)
# % -> __mod__
# ** -> __pow__

class Cifra: 
    def __new__(cls, *args, **kwargs):
        print(cls, '!!!!')
        number = abs(args[0]) #вызываем абсолютное число
        instance = super().__new__(cls) # insrance = Cifra()
        instance.number = number
        return instance 
    

    def __add__(self, other): 
        print('add worked')
        res = self.number + other.number 
        print(f'Result: {self.number} + {other.number} = {res}')
        return res 

value1 = Cifra(-123, 767, 7655)
value2 = Cifra(54)
res = value1 + value2
print(res)


__________________________________________________________
from random import choice 

class Dog: 
    def sound(self): 
        print('Bark!')

    
class Cat: 
    def sound(self): 
        print('meow meow')

class Horse:
    def sound(self): 
        print('Igo-go-go!')

class Pet: 
    def __new__(cls):
        pet = choice([Dog,Cat,Horse])
        self = super().__new__(pet)
        print(f'I\'m {type(self).__name__}')
        return self

    def __init__(self):
        print('Pet never was called!')

pet = Pet()
pet.sound()

______________________________________________________________________
# SINGLETON

class Singleton: 
    _instance = None 

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __str__(self) -> str:
        return str(id(self))
    
a = Singleton()
b = Singleton()
print(a,b)
print(a is b)
obj = Singleton()
obj1 = Singleton()
print(obj, obj1)

______________________________________________________________________________
from itertools import repeat
from random import choice, randint

class Kopilka: 
    def __init__(self) -> None:
        self.total = 0
        self.coins = []

    def add_coins(self, coin): 
        self.total += coin 
        self.coins.append(coin)

    def __len__(self): 
        return len(self.coins)
    
    def __getitem__(self, index): 
        return self.coins[index -1]



obj = Kopilka()

for f in repeat(choice, randint(89, 134)):
    obj.add_coins(f([1,3,5,10]))
obj.add_coins(10)
obj.add_coins(5)
obj.add_coins(3)
obj.add_coins(1)

print(obj.coins)
print(obj.total)

print(len(obj))
print(obj[7])

for x in obj: 
    print(x)


        

