

# 1) Палиндром:

# slovo = str(input()).lower()
# a = slovo[::-1]
# if slovo == a:
#   print("yes")
# else:
#   print("no")

# 2) Подсчет слов:
# txt =  'Привет мир! Меня зовут Python'
# res= txt.split(' ')
# print(res)
# print(len(res))

# 3) Генерация пароля:
# import random 
# import string

# symbol = string.ascii_letters + string.digits + string.punctuation
# symbol = [i for i in symbol]

# password = []
# dlina = int(input('Введите длину:'))

# for i in range(dlina):
#     random_sym = random.choice(symbol)
#     password.append(random_sym)
# print(''.join(password))


# 5) Подсчет гласных и согласных:
# slovo = input('Введите слово:')
# glasnyie = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
# i= 0
# gls = 0 
# sgl = 0 
# for i in slovo:
#     if i in glasnyie:
#         gls+=1
#     else:
#         sgl+=1
# print(gls,sgl)

# 4) Поиск повторяющихся символов:

# flag = 'net'

# slovo = input('Введите слово:')
# for i in slovo: 
#     if slovo.count(i)> 1:
#         flag = 'da est'

# print(flag)

# ________________________________________________________________________________________________________

# sen = 'Привет мир! Меня зовут Python'
# print(sen[0], sen[0-1])
# res1 = sen[7:10].split(' ')
# print(res1)
# res2 = sen[::-1].split(' ')
# print(res2)
# print(''.join(sen[::2]))


# first_name =input('name:')
# last_name = input('surname:')
# age = input('age:')
# print(f'{first_name} {last_name} {age}')
# print('Name: %s, Surname %s! He is %s'%(first_name,last_name,age))
# print('Name: {}, Surname {}! is {}'.format(first_name,last_name,age))


# text = "Программирование на Python - это увлекательно!"
# res3 = text.replace('Python','JavaScript')
# print(res3)
# print(text.isalpha())
# print(text.index('а'))

# txt = "Строки - это базовый тип данных в Python."
# print(txt.count('Python'))
# res4= txt.split(' ')
# print(res4)
# print(txt.swapcase())

