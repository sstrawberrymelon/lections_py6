# 1) Умножение соответствующих элементов двух списков: 
# Используйте map и lambda, чтобы умножить соответствующие элементы двух списков.

# list1=[1,2,3,4,5]
# list2=[5,4,3,2,1]
# def Product(list1,list2): 
#     if len(list1) != len(list2): 
#         raise ValueError("Списки должны быть одинаковой длины!")

#     return list(map(
#         lambda x,y: x*y,list1,list2))
# print(Product(list1,list2))

# 2) Проверка, что в строке есть хотя бы одна гласная буква: 
# Используйте any и lambda, чтобы проверить, что в строке есть хотя бы одна гласная буква.

# letters=['a','e','i','o','u','y']
# def func(text):
#     return any (char in letters for char in text.lower())
# print(func(input('Введите текст:')))


# 3) Фильтрация слов с определенной длиной: Используйте filter и 
# lambda для фильтрации слов в списке строк, имеющих заданную длину.

# ls = ['John','Kare','Kira','Raychel','Gloria','Marta']
# res = list(filter(lambda x: len(x)>4,ls))
# print(res)

# 4) Проверка, что все элементы списка больше нуля: Используйте all и map, 
# чтобы проверить, что все элементы в списке больше нуля.

# ls = [1,2,3,4,5]
# res = all(map(lambda x: x>0, ls))
# print(res)

# 5) Сумма квадратов четных чисел: Напишите программу, которая с использованием 
# map и reduce находит сумму квадратов четных чисел в списке.

# from functools import reduce

# ls = [1,2,3,4]

# even = list(filter(
#     lambda x: x % 2 == 0, ls ))
# square = list(map(
#     lambda x: x **2 , even ))
# res = reduce(
#     lambda x,y: x + y, square)
# print(res)


# import telebot
# bot = telebot.TeleBot('1890538331:AAGxF21EUfiAU56_mZAdpH-ZkmxytR3qG7I')
# @bot.message_handler(commands = ['start']) #команда для бота
# def start(message):
#     bot.send_message(message.chat.id, 'hello<3')
# @bot.message_handler(commands = ['howRU'])
# def howRU(message):
#     bot.send_message(message.chat.id, 'swag')
# @bot.message_handler(commands = ['info'])
# def info(message):
#     bot.send_message(message.chat.id, 'My name is Bot 1501')
# @bot.message_handler(commands = ['photo'])
# def send_photo(message):
#     bot.send_photo(message.chat.id,'https://i.pinimg.com/236x/13/86/ec/1386ecb6232a68915a8c5b04674556f4.jpg')

# @bot.message_handler(content_types=['text'])
# def send_answer(message):
#     if message.text == 'Привет':
#         bot.send_massage(message.chat.id, 'hello<3')
#     elif message.text == 'Как дела?':
#         bot.send_message(message.chat.id, 'Swag')


# bot.polling(none_stop=True)