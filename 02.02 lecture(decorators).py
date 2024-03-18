# # decorator - это функция(как обертка)

# import requests 
# from time import time 
# def timeCheck(func):
#     def wrapper():
#         start = time() #10:26:12
#         func()
#         finish = time() #10:26:32
#         print(f'Time to get result:{round(finish-start, 2)}')
#     return wrapper


# @timeCheck #обертка printCars 
# def printCars():
#     car = input('Enter car model:')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR:{response.status_code}{response.text}')
# @timeCheck
# def printUser():
#     api_url = 'https://randomuser.me/api'
#     response = requests.get(api_url)
#     print(response)
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR: {response.status_code} \n {response.text}')

# printUser()
# print()
# print()
# printCars()

# def decorator(func): 
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func.__name__} была вызвана!')
#         print()
#         func()
#     return wrapper 

# @decorator
# def get_name():
#     print(f'Owner name is John Snow!')
# get_name()

# def trace(func):
#     def wrapper(*args,**kwargs):
#         print(f'Tarce: вызвала {func.__name__}()\n она приняла args: {args}, kwargs: {kwargs}')
#         res = func(*args,**kwargs)
#         print(f'Tarce: вызвала {func.__name__}()\n она вернула {res}')
#         return res 
#     return wrapper 

# @trace 
# def getAdress(name,adress):
#     return f'Name: {name} -> Adress: {adress}'
# @trace 
# def getHello(name,last_name,country):
#     return f'Hello {name} {last_name} from {country}'

# print(getAdress('Vin winchester','Kansas'))
# print()
# print(getHello('Sam', last_name='Winchester', country='USA'))


# def bold(func):
#     def wrapper(*args,**kwargs):
#         res = '<bold>' + func(*args,**kwargs) +'</bold>'
#         return res 
#     return wrapper 

# def iText(func):
#     def wrapper(*args,**kwargs): 
#         res = "<i>" + func(*args,**kwargs) + '<i>'
#         return res
#     return wrapper  

# @iText
# @bold
# def get_name():
#     name = input('Vvedite svoyo imya:')
#     return name

# print(get_name())









