# decorators
# Декаратор - это функция, которая позволяет без изменения кода функции расширить ее фукнционал. 

# import requests

# def printCars():
#     car = input('Enter car model:')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR:{response.status_code}{response.text}')



# def printUser():
#     api_url = 'https://randomuser.me/api'
#     response = requests.get(api_url)
#     print(response)
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'ERROR: {response.status_code} \n {response.text}')

# printUser()



# Заядлый турист ведет тщательный учет своих походов. 
# Во время последнего похода, который занял ровно шаги, 
# за каждым шагом отмечалось, был ли это подъем в гору ,, 
# или спуск ,шаг. Походы всегда начинаются и заканчиваются
# на уровне моря, и каждый шаг вверх или вниз представляет 
# собойизменение единицы высоты. Мы определяем следующие термины:
# # Гора – это последовательность последовательных ступенек над уровнем моря, 
# начиная со ступеньки вверх от уровня моря и заканчивая ступенькой вниз до уровня моря.
# # Долина — это последовательность последовательных ступеней ниже уровня моря,
#  начиная со ступеньки вниз от уровня моря и заканчивая ступенькой вверх до уровня моря.
# # Зная последовательность подъемов и спусков во время похода, найдите 
# и выведите количество пройденных долин .
# пример 1:
# path = 8
# steps= 'UDDDUDUU'
sea_level = 0
dolina = 0 
#  result = 1 dolina
# пример 2:
#  path = 10
steps = 'DUDDDUUDUUDUDUDUDUDU'
#  result = 2 dolina

for step in steps: 
    if step == 'U':
        sea_level += 1
        if sea_level == 0:
            dolina += 1
    else:
        sea_level -= 1

print(f'{dolina} долины')
    
    
