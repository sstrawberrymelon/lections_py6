# Инкапсуляция 
# 1. Языковая контрукция, которая помогает связать данные с методами для их обработки и управления
# (связь между данными и методами которые управляют ими)(класс-капсула)
# 2. Механизм сокрытия, при помощи которого можно ограничить доступ одного компонента программы 
# к другмоу 

# Инкапсуляуция как связь
# class Phone:
#     number ='+9987667788'

#     def print_number(self): 
#         print(f'Moi nomer:{self.number}') 
#         print(f'Moi nomer:{Phone.number}') 
# p = Phone()
# p.print_number()


# Инкапсуляция как механизм сокрытия 
# 3 уровня сокрытия данных в питоне 
# 1. Публичный(public) - number, print_number
# 2. Защищенный(_protected) - _number
# 3. Приватный(_private) - __number

# class Car: 
#     _country = 'Germany'
#     __motor  = 'GT Line'

#     def __init__(self) -> None:
#         self.marka = 'BMW' #public
#         self._model = 'I8' #protected
#         self.__color = 'black' #private

# obj = Car()
# print(dir(obj))

# print(obj.marka)
# print(obj._country,obj._model)
# print(obj._Car__color,obj._Car__motor) #обходной путь для выявления приватных 


# class Phone: 
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 17

#     def call(self): 
#         print(f'{self._caller} звонит вам!')
#         question = input('Взять трубку(yes/no): ')
#         if question.lower().strip() == 'yes': 
#             self.__turn.on()
#         else:
#             print('сбросили трубку')

#     def __turn_on(self): 
#         self.__increment_calls()
#         print('Allo')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

#     def __increment_calls(self): 
#         self.__count_of_calls +=1

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()
# john.call()
# john.call()

# _________________________________________________________
# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name 
#         self.age = age

#     def display_info(self): 
#         print(f'My name is {self.name} and I\'m {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.name = [1,2,3,4]
# obj.age = -25     
# obj.display_info()
# _______________________________________________________________________________
# getter & setter
# они нужны чтобы избежать прямого обращения к сокрытым атрибутам
# при этом можно добавить логику валижация(проверки) данных которые будут установлены в атрибут


class Person:
    def __init__(self, name, age) -> None:
        self.__name = name 
        self.__age = age

    def display_info(self): 
        print(f'My name is {self.__name} and I\'m {self.__age} years old!')



    #getter
    def name(self): return self.__name 
    def age(self): return self.__age

    #setter
    def set_name(self, name): 
        if not isinstance(name, str): 
            print('Name must be str object!')
        else:
            self.__name = name 


    def set_age(self, age): 
        if not isinstance(age, int) or not 0 <=age < 150:  
            print('Invalid value for age!')
        else:
            self.__age = age 

obj = Person('John', 24)
obj.display_info()
obj.set_name(55)
obj.display_info()
obj.set_age(26)
obj.display_info()



