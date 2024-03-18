# Анотация свойств (@property(getter setter))

# class Person: 
#     __name = 'John'
#     __age = 22

#     @property 
#     def name(self): 
#         """The name property(getter)"""
#         print(self.__name)
    
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str): 
#             print('Invalid value for name!')
#         else:
#             print(f'Setter, {value}')
#             self.__name = value 
#     @property 
#     def age(self): 
#         print(self.__age)

#     @age.setter
#     def age(self,value):
#         if not isinstance(value, int) or value not in range(0,150):
#             print('Invalid value for age')
#         else: 
#             self.__age = value

# obj = Person()
# obj.name
# obj.name = 'Din Winchester'
# obj.name 
# obj.age 
# obj.age = 24
# obj.age


# ____________________________________________________________________________________

# read, write, delete

# class Circle:
#     def __init__(self,radius) -> None:
#         self._radius = radius 
    
#     def _get_radius(self):
#         print('getter,_get_radius')
#         return  self._radius
    
#     def _set_radius(self,value): 
#         print('setter,_set_radius')
#         if not isinstance(value,(int,float)):
#             print('Invalid radius must be an int or float object')
#         else:
#             self._radius = value
        
#     def _del_radius(self):
#         print('del, _del_radius')
#         answer = input("Sre you dure")
#         if answer.lower().strip()== 'yes':
#             del self._radius
#             print('deleted')
#         else:
#             print('not deleted')
    
#     radius = property(fget = _get_radius,fset = _set_radius, fdel =_del_radius, doc ='radius property' )

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7.5
# print(obj.radius)

# ______________________________________________________________________________________
# read-only

# class CoordinateWriteError(Exception):
#     pass

# class Point: 
#     def __init__(self,x,y) -> None:
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         print(self.__x)

#     @property
#     def y(self):
#         print(self.__y)

#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError('x coordinate is read-only!')
    
#     @y.setter
#     def y(self, value):
#         raise CoordinateWriteError('y coordinate is read-only!')

# obj = Point(42.2313, - 12.12314)
# obj.x
# obj.y


# _______________________________________________________________________________
# write-only 

import hashlib #
import os #

class User: 
    def __init__(self, username, password):
        self.username = username 
        self.__password = password

    @property
    def password(self):
        raise AttributeError('Password is write-only!')

    @password.setter
    def password(self, value): 
        if not isinstance(value, str) or len(value)<8:
            raise ValueError('invalid value for password!')       
        salt =os.urandom(32)
        self.__password = hashlib.pbkdf2_hmac('sha256',value.encode('utf-8'),salt, 100_000)

john = User('john snow', 'secretkey')
# print(john.password)
john.password = 'JohnSnowTheBest'
print(john._User__password)





























