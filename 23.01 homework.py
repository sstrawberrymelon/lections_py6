# Напишите программу, которая симулирует игру лото с 
# одной картой. Начните с генерирования списка их всех возможных
# номеров выпадения (от В1 до О75). После этого перемешайте номера в
#  хаотичном порядке, воспользовавщись функцией shuffle из модуля random. 
#  Вытаскивайте по одному номеру из списка и зачеркивайте номера, пока карточка не 
#  окажется выигравшей. Приведите 1000 симуляций и выведите на экран минимальное, 
#  максимальное и среднее количество извлечений номеров, требующееся для выигрыша.


# import random


# numbers = []
# for i in range(1, 91):
#     numbers.append(f"В{i}")
# for i in range(91, 99):
#     numbers.append(f"Г{i - 90}")
# for i in range(99, 100):
#     numbers.append(f"Д{i - 99}")
# for i in range(100, 101):
#     numbers.append(f"Е{i - 100}")
# for i in range(101, 102):
#     numbers.append(f"Ж{i - 101}")
# for i in range(102, 103):
#     numbers.append(f"З{i - 102}")
# for i in range(103, 104):
#     numbers.append(f"И{i - 103}")


# random.shuffle(numbers)


# results = []
# for _ in range(1000):
    
#     card = random.sample(numbers, 5)
#     count = 0
#     for number in numbers:
#         count += 1
#         if number in card:
#             break
#     results.append(count)


# print(f"Минимальное количество извлечений: {min(results)}")
# print(f"Максимальное количество извлечений: {max(results)}")
# print(f"Среднее количество извлечений: {sum(results) / len(results)}")




import string

morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}


string_ = input("Введите строку: ")

encoded_string = 0
for symbol in string_:
    if symbol in string.ascii_lowercase:
        encoded_string += morse_code[symbol]
    elif symbol in string.digits:
        encoded_string += morse_code[symbol]
    else:
        encoded_string += symbol


print(encoded_string)