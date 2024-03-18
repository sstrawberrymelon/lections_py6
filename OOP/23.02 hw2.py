# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, 
# краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % 
# заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

class Smartphone: 
    prevbatlev = 100

    def __init__(self,imei, batlev, os):
        self.imei = imei 
        self.batlev = batlev
        self.os = os 
        if batlev == 100: 
            raise SystemError('Battery low! Please charge!')
        
    def get_info(self): 
        self.batlev -= 0.5
        return f'Imei:{self.imei}, Battery level:{self.batlev},Operating system:{self.os}'
            

    def lismusic(self): 
        self.batlev -=5
        return f'Battery level is {self.batlev}%'
    
    def watchvid(self): 
        self.batlev -=7
        if self.batlev < 10:
            print('Low battery! Video can not be played!')
        else:
            return f'Battery level is {self.batlev}%'
        
    def charge(self): 
        self.batlev = 99
        return 'Your phone is charged!' 
    
        

a = Smartphone(123, 12, 'ios')
print(a.lismusic())
print(a.watchvid())
print(a.charge())
print(a.get_info())






    
    



