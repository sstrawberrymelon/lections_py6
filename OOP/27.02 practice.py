# 1)Создайте класс и объявите в нём 3 метода: публичный, защищённый и приватный. 
# Затем создайте экземпляр данного класса и вызовите по очереди каждый из методов.
# """




class Animal: 
    def __init__(self, name, age, color) -> None:
        self.name = name 
        self._age = age
        self.__color = color

    def __str__(self): 
        return f'Name:{self.name} Age:{self.age},Color:{self.color}'

obj = Animal('Cat', 2,'white')
print(obj)



# """
# 2)Определите класс A, в нём объявите метод method1, который печатает строку "Hello World". 
# Затем создайте класс B, который будет наследоваться от класса A. 
# Создайте экземпляр от класса B, и через него вызовите метод method1.
# """
# # писать код здесь

# """
# 3)Объявите класс Car, в котором будет приватный атрибут экземпляра speed. 
# Затем определите метод set_speed, который будет устанавливать значение скорости 
# и метод show_speed, с помощью которого Вы будете получать значение скорости.
# """
# # писать код здесь

# """
# 4)Перепишите класс Car из предыдущего задания.
# Перепишите метод set_speed() с использование декоратора @speed.setter, 
# а метод show_speed() с использованием декоратора @property, для того чтобы 
# можно было работать с данным классом следующим образом:

# car = Car()
# car.speed = 120
# print(car.speed)
# """
# # писать код здесь

# """
# 5. Создайте класс Car. Пропишите в init параметры make, model, year, odometer, fuel.
# Пусть у показателя odometer будет первоначальное значение 0, а у fuel 70.
# Добавьте метод drive, который будет принимать расстояние в км. В самом начале проверьте,
# хватит ли вам бензина из расчета того, что машина расходует 10 л / 100 км (1л - 10 км) . Если
# его хватит на введенное расстояние, то пусть этот метод добавляет эти километры к значению
# одометра, но не напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью приватного
# метода __subtract_fuel, затем пусть распечатает на экран “Let’s drive!”. Если же бензина не 
# Let’s drive!”. Если же бензина не
# хватит, то распечатайте “Let’s drive!”. Если же бензина не Need more fuel, please, fill more!”
# """
# # писать код здесь
# """