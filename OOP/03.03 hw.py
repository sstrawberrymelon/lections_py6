
# Задача 1: "Dollar"

#     Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
#     Описание:
#         Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.
#         Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
#         Пример использования:
#         # cash = MoneyFmt(12345678.021) 
#         # print(cash) -- выводит "$12,345,678.02" 
#         # cash.update(100000.4567) 
#         # print(cash) -- выводит "$100,000.46" 
#         # cash.update(-0.3) 
#         # print(cash) -- выводит "-$0.30" 
#         # repr(cash) -- выводит -0.3 


def dollarize(num):
    return str(num)

class MoneyFmt:
    def __init__(self, money):
        self.amount = round(money,2)
        
    def update(self, new_value):
        self.amount = new_value

    def __str__(self) -> str:
        return dollarize(self.amount)
    
    def doll_format(self): 
        ind = str(self.amount).index('.')
        osn = str(self.amount)[:ind]
        end = str(self.amount)[ind+1:]
        osn = [i for i in osn[::-1]]
        
        for i in range(3, len(osn), 4):
            osn.insert(i, ',')
        osn = ''.join(osn[::-1])
        res = osn + '.' + end

        return res

        
    

cash = MoneyFmt(0.021) 

print(cash.doll_format())
    

# __________________________________________________________________________________________
# Задача 2: "Велосипед"

#     Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
#     Описание:
#         Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
#         Методы должны позволять устанавливать цену продажи, учитывая минимальную прибыль, обслуживать велосипед, изменяя его состояние и стоимость ремонта, и продавать велосипед, изменяя его статус и рассчитывая прибыль.

class Bike:
    def __init__(self, price, creator, model, year, condition, sell_price=0, sell_status=False) -> None:
        self.price = price 
        self.creator = creator 
        self.model = model 
        self.year = year 
        self.condition = condition
        self.sell_price = sell_price
        self.sell_status = sell_status

    def min_income_price(self):
        min_income = self.price * (10/100)
        self.sell_price = self.price + min_income
        return f'Min income sell price:{self.sell_price}'
    
    def fix_bycacle(self, remont): 
        self.remont = remont 
        self.condition = 'good'
        return f'Состояние велосипеда:{self.condition}'
    
    def sell_bycycle(self):
        self.sell_status = True
        income = self.sell_price - (self.remont + self.price)
        return f'Прибыль: {income}'

    def __str__(self) -> str:
        return f'Цена:{self.price},Производитель:{self.creator},Модель:{self.model},Год:{self.year},Состояние:{self.condition},Продажная цена:{self.sell_price},Статус:{self.sell_status}'
    
bike = Bike(12000,'Galaxy',790, 2017, 'ploho')
print(bike.min_income_price())
print(bike.fix_bycacle(300))
print(bike.sell_bycycle())

        



    






        








# _____________________________________________________________________________________
# Задача 3: "Герой"

#     Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
#     Описание:
#         Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
#         Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
#         В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.



# class Soldier:
#     def __init__(self, team_id, unique_id):
#         self.team_id = team_id
#         self.unique_id = unique_id
#         self.following_hero = None

#     def follow_hero(self, hero):
#         if self.team_id == hero.team_id:
#             self.following_hero = hero

# class Hero:
#     def __init__(self, team_id, unique_id):
#         self.team_id = team_id
#         self.unique_id = unique_id
#         self.level = 1
#         self.soldiers = []

#     def level_up(self):
#         self.level += 1

# def generate_soldiers(team_id, count):
#     return [Soldier(team_id, i) for i in range(count)]

# def main():
#     team_1_soldiers = generate_soldiers(1, 10)
#     team_2_soldiers = generate_soldiers(2, 15)

#     hero_1 = Hero(1, 1)
#     hero_2 = Hero(2, 2)

#     for soldier in team_1_soldiers:
#         soldier.follow_hero(hero_1)

#     for soldier in team_2_soldiers:
#         soldier.follow_hero(hero_2)

#     if len(team_1_soldiers) > len(team_2_soldiers):
#         hero_1.level_up()
#     else:
#         hero_2.level_up()

#     print(f"Уровень героя команды 1: {hero_1.level}")
#     print(f"Уровень героя команды 2: {hero_2.level}")


    



    
    

        
