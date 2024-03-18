from views import CreateMixin, ReadMixin


class Smartphones(CreateMixin, ReadMixin): 
    pass 

smartphones = Smartphones()
print(smartphones.post(title='Redmi Note 10',description='The best phone for own price!',qty=10,price=250))

print(smartphones.post(title='iphone 15 pro max',description='The best for taking photos',qty=3,price=1200))

print(smartphones.post(title='Lenovo Si',description='The best in China',qty=11,price=150))

print(smartphones.post(title='Samsung Ulstra S7',description='The best phone in Korea',qty=2,price=700))

print(smartphones.post(title='Google 132',description='The best phone in California',qty=6,price=467))

print()
print()
print(smartphones.list())
print()
print(smartphones.detail(3))
print()
