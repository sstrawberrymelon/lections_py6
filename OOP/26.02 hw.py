# Напишите класс Subscriber, у которого есть переменные экземпляра:
# firstname
# lastname
# Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
# Напишите класс Provider, у которого есть:
# переменный экземпляра name -- название провайдера
# переменный экземпляра subscribers -- список, в котором будут храниться экземпляры 
# класса Subscriber
# переменный экземпляра payments -- словарь, ключём которого является экземпляр класса 
# Subscriber, значением является сумма (вещественное число)
# метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем 
# проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
# Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве
# значения
# Если нет, выкидывает (raise) ошибку ValueError
# Напишите класс Terminal, у которого есть
# переменная экземпляра amount = 0
# переменная экземпляра providers = [ ]
# Регистрировать провайдера через метод register, который принимает экземпляр класса Provider
# и добавляет в providers
# Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, 
# экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться 
# метод register_payment экземпляра класса Provider. register_payment успешно сработал, 
# то в переменую amount нужно добавить сумму.


class Subscriber: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __repr__(self):
        return self.firstname +' '+ self.lastname
    
class Provider: 
    def __init__(self,name,subscribers):
        self.name = name
        self.subscribers = [subscribers]
        self.payments = {}


    def register_payment(self, subscriber, amount): 
        if subscriber in self.subscribers: 
            self.payments[subscriber] = amount
        else: 
            raise ValueError
        
    def __repr__(self):
        return f"Provider {self.name} with {len(self.subscribers)} subscribers and {len(self.payments)} payments"

class Terminal: 
    def __init__(self, amount=0 ):
        self.amount = amount
        self.providers = []

    def register(self, provider):
        self.providers.append(provider)

    def pay(self, subscriber, provider, amount):
        provider.register_payment(subscriber, amount)
        self.amount += amount 

    def __repr__(self) -> str:
        return f"Terminal with {len(self.providers)} providers and {self.amount} total amount"
    

some_sub = Subscriber('anrbek', 'tima')
some_provider = Provider('Beeline', some_sub)
some_provider.register_payment(some_sub, 2000)
print(some_provider.payments)
terminal = Terminal()
terminal.register(some_provider)
terminal.pay(some_sub,some_provider, 2000)
print(terminal)







        


