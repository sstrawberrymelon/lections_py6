"""1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on
a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект 
и вызовите все методы.
"""
# class Auto: 
#     def ride(self): 
#         return 'Riding on the ground'
    
# class Boat: 
#     def swim(self): 
#         return 'Floating on Water'
    
# class Amphibian(Auto,Boat):
#     pass

# obj = Amphibian()
# print(obj.swim())
# print(obj.ride())







"""2) Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music
который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте 
функционал этих классов при помощи миксина"""
# class RadioMixin:
#     def play_music(self, name):
#         self.name = name
#         return name 

# class Auto(RadioMixin): 
#     pass
    

# class Boat(RadioMixin): 
#     pass
    

# class Amphibian(RadioMixin): 
#     pass
    
# obj = Amphibian()
# print(obj.play_music('MAGIC SHOP'))

"""3) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, 
с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
# from datetime import datetime
# class Clock:
#     def time(self):
#         return f'Time:{datetime.now()}'


# class Alarm(Clock): 
#     def turn_on(self):
#         return 'ON'
    
#     def trun_off(self): 
#         return 'OFF'
    
    
# class AlarmClock(Alarm,Clock):
#     def set(self, time):
#         super().time()
#         self.time = time
#         return f'Alarm is {self.turn_on()}'
    

# obj = AlarmClock()
# print(obj.set('14:32'))

    

"""4) Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. 
Класс Backend должен принимать дополнительно параметр languages_backend, а 
Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал 
количество часов кодинга и при каждом вызове этого метода добавлял это значение 
к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. 
Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

# class Coder: 
#     def __init__(self, experience, count_code_time = 0) -> None:
#         self.experience = experience
#         self.count_code_time = count_code_time

#     def coding(self):
#         self.experience += self.count_code_time
#         return f'Code time:{self.experience}'

#     def get_info(self): 
#         return f'Время:{self.coding()}'


# class Backend(Coder): 
#     def __init__(self, experience, languages_backend=[]) -> None:
#         Coder.__init__(self, experience)
#         self.languauges_backend = languages_backend


# class Frontend(Coder): 
#     def __init__(self, experience,languages_frontend=[]) -> None:
#         Coder.__init__(self, experience)
#         self.languages_frontend = languages_frontend

# class FullStack(Backend, Frontend):
#     def __init__(self, experience,languages_backend=[], languages_frontend=[]) -> None:
#         Backend.__init__(self, experience, languages_backend)

#         Frontend.__init__(self, experience, languages_frontend)

        
# person = FullStack(7,'Python, PhP','JS')
# print(person.coding())
